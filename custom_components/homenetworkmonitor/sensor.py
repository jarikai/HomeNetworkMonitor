"""Sensor platform for HomeNetworkMonitor."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.util import dt as dt_util

from .const import DOMAIN
from .entity import HomeNetworkMonitorEntity

if TYPE_CHECKING:
    from datetime import datetime

    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import HomeNetworkMonitorDataUpdateCoordinator
    from .data import HomeNetworkMonitorConfigEntry

_LOGGER = logging.getLogger(__name__)

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="homenetworkmonitor_nmaprun_scaninfo",
        name="Nmap run scan info",
        icon="mdi:information-outline",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_hosthint",
        name="Nmap basic host info",
        icon="mdi:computer-network",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_host",
        name="Nmap Host data",
        icon="mdi:computer-network",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_postscript",
        name="Nmap postscript data",
        icon="mdi:information-outline",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_runstats",
        name="Nmap runstats data",
        icon="mdi:information-outline",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_port",
        name="Nmap host port data",
        icon="mdi:port-hole",
    ),
)


def parse_datetime(value: str | None) -> datetime | None:
    """Parse datetime string."""
    if value is None:
        return None

    return dt_util.parse_datetime(value)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HomeNetworkMonitorConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    coordinator = entry.runtime_data.coordinator
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
    entities = []
    # Add the main sensors

    # Keep track of host entities to manage updates
    host_entities = []

    # Add a listener to update host sensors when data is available
    def async_update_host_sensors() -> None:
        """Update host sensors when coordinator data changes."""
        # Remove existing host sensors
        for entity in host_entities[:]:  # Use a copy of the list
            if entity in entities:
                entities.remove(entity)
                host_entities.remove(entity)

        # Add new host sensors if data is available
        if coordinator.data and "host" in coordinator.data:
            seen_unique_ids = set()
            # Handle both old and new structure formats
            hosts_data = coordinator.data["host"]
            if isinstance(hosts_data, list):
                host_list = hosts_data
            else:
                # If it's a dict with hosts as a key
                host_list = (
                    hosts_data.get("host", []) if isinstance(hosts_data, dict) else []
                )

            for host_data in host_list:
                try:
                    host_entity = Host(coordinator, ENTITY_DESCRIPTIONS[2], host_data)
                    if host_entity.unique_id not in seen_unique_ids:
                        entities.append(host_entity)
                        host_entities.append(host_entity)
                        seen_unique_ids.add(host_entity.unique_id)
                        # add Port entities for each host

                        ports_data = host_data.get("os", {}).get("portused", [])
                        if ports_data is not None:
                            for port_data in ports_data:
                                port_entity = Port(
                                    coordinator,
                                    ENTITY_DESCRIPTIONS[5],
                                    port_data,
                                    ip_address=host_data.get("address", "unknown")[
                                        0
                                    ].get("addr", "unknown"),
                                )
                                if port_entity.unique_id not in seen_unique_ids:
                                    entities.append(port_entity)
                                    host_entities.append(port_entity)
                                    seen_unique_ids.add(port_entity.unique_id)
                except Exception:
                    _LOGGER.exception("Error creating host entity:")
        else:
            _LOGGER.debug("No host data available to create host sensors.")

    # Add the listener to the coordinator
    entry.async_on_unload(coordinator.async_add_listener(async_update_host_sensors))

    # Initial call to set up host sensors if data is already available
    async_update_host_sensors()

    # Add main sensors
    host_hint_data = coordinator.data.get("hosthint", {})
    if host_hint_data:
        entities.append(
            NmapHostsSensor(coordinator, ENTITY_DESCRIPTIONS[1], host_hint_data)
        )

    entities.append(NmapScanInfoSensor(coordinator, ENTITY_DESCRIPTIONS[0]))
    post_script_data = coordinator.data.get("postscript", {})
    if post_script_data:
        entities.append(
            NmapPostScriptSensor(coordinator, ENTITY_DESCRIPTIONS[3], post_script_data)
        )
    runstats_data = coordinator.data.get("runstats", {})
    if runstats_data:
        entities.append(
            NmapRunstatsSensor(coordinator, ENTITY_DESCRIPTIONS[4], runstats_data)
        )

    async_add_entities(entities, update_before_add=True)


class NmapRunstatsSensor(HomeNetworkMonitorEntity, SensorEntity):
    """Sensor for Nmap scanning result output."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        runstats_data: dict,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._runstats_data = runstats_data or {}
        self._attr_unique_id = f"{DOMAIN}_{self.entity_description.key}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}

        if self._runstats_data:
            finished = self._runstats_data.get("finished", {})
            if finished:
                attributes["time"] = finished.get("time", "unknown")
                attributes["timestr"] = finished.get("timestr", "unknown")
                attributes["elapsed"] = finished.get("elapsed", "unknown")
                attributes["summary"] = finished.get("summary", "unknown")
                attributes["exit"] = finished.get("exit", "unknown")
            hosts = self._runstats_data.get("hosts", {})
            if hosts:
                attributes["up"] = hosts.get("up", "unknown")
                attributes["down"] = hosts.get("down", "unknown")
                attributes["total"] = hosts.get("total", "unknown")

        return attributes

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "Devices"

    @property
    def state(self) -> int | None:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return None
        return len(self._runstats_data)

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"homenetworkmonitor_{self.entity_description.key}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="Home Network Monitor",
            manufacturer="Jari Kaipio",
            model="Local Network Scanner",
            configuration_url=self.coordinator.config_entry.data.get("url", ""),
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def should_poll(self) -> bool:
        """Return True as updates are needed."""
        return True


class NmapPostScriptSensor(HomeNetworkMonitorEntity, SensorEntity):
    """Sensor for Nmap scanning result output."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        post_script_data: dict,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._post_script_data = post_script_data or {}
        self._attr_unique_id = f"{DOMAIN}_{self.entity_description.key}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}

        if isinstance(self._post_script_data, dict):
            attributes["id"] = self._post_script_data.get("id", "unknown")
        elif isinstance(self._post_script_data, list) and self._post_script_data:
            script = self._post_script_data[0]
            attributes["id"] = script.get("id", "unknown")
            attributes["output"] = script.get("output", "unknown")

        return attributes

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "Devices"

    @property
    def state(self) -> int | None:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return None
        return len(self._post_script_data)

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"homenetworkmonitor_{self.entity_description.key}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="Home Network Monitor",
            manufacturer="Jari Kaipio",
            model="Local Network Scanner",
            configuration_url=self.coordinator.config_entry.data.get("url", ""),
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def should_poll(self) -> bool:
        """Return True as updates are needed."""
        return True


class NmapHostsSensor(HomeNetworkMonitorEntity, SensorEntity):
    """Sensor for Nmap scanned hosts."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        host_data: dict,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._attr_unique_id = f"{DOMAIN}_{self.entity_description.key}"
        self._host_data = host_data or {}

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "Devices"

    @property
    def state(self) -> int | None:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return None
        return len(self._host_data)

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"homenetworkmonitor_{self.entity_description.key}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="Home Network Monitor",
            manufacturer="Jari Kaipio",
            model="Local Network Scanner",
            configuration_url=self.coordinator.config_entry.data.get("url", ""),
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def should_poll(self) -> bool:
        """Return True as updates are needed."""
        return True


class NmapScanInfoSensor(HomeNetworkMonitorEntity, SensorEntity):
    """Sensor for Nmap scan information."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._attr_unique_id = f"{DOMAIN}_{self.entity_description.key}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}
        scan_info = self.coordinator.data.get("scaninfo", {})
        if scan_info:
            attributes["scan_type"] = scan_info.get("type", "unknown")
            attributes["protocol"] = scan_info.get("protocol", "unknown")
            attributes["num_services"] = scan_info.get("numservices", "unknown")

        return attributes

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return "unknown"

        scan_info = self.coordinator.data.get("scaninfo", {})
        result = "unknown"

        if len(scan_info) > 0:
            result = "OK"

        return str(result)

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"homenetworkmonitor_scan_info_{self.coordinator.config_entry.entry_id}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="Home Network Monitor",
            manufacturer="Jari Kaipio",
            model="Local Network Scanner",
            configuration_url=self.coordinator.config_entry.data.get("url", ""),
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def should_poll(self) -> bool:
        """Return True as updates are needed."""
        return True


class Host(HomeNetworkMonitorEntity, SensorEntity):
    """Sensor for individual host information."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        host_data: dict,
    ) -> None:
        """Initialize the host sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._host_data = host_data or {}

        # Extract IP address from the new JSON structure
        self._ip = "unknown"
        # Handle case where host_data might be a list
        if isinstance(self._host_data, list):
            # If it's a list, take the first item or use empty dict
            self._host_data = self._host_data[0] if self._host_data else {}

        # Now safely extract IP address
        self._ip = self._host_data.get("ip", "unknown")
        if not self._ip or self._ip == "unknown":
            address_data = self._host_data.get("address", {})
            if isinstance(address_data, dict):
                self._ip = address_data.get("addr", "unknown")
            elif isinstance(address_data, list) and len(address_data) > 0:
                # Handle case where address is a list
                first_addr = address_data[0]
                if isinstance(first_addr, dict):
                    self._ip = first_addr.get("addr", "unknown")
        if not self._ip or self._ip == "unknown":
            self._ip = self._host_data.get("addr", "unknown")

        self._attr_unique_id = f"{DOMAIN}_host_{self._ip}"

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        if self._attr_unique_id is not None:
            return self._attr_unique_id
        return f"homenetworkmonitor_host_{self._ip}"

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        status_data = self._host_data.get("status", {})
        if isinstance(status_data, dict):
            return status_data.get("state", "unknown")
        return "unknown"

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"Host {self._ip}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}
        if self._host_data:
            attributes["ip"] = self._ip
            attributes["status"] = self._host_data.get("status", "unknown")
            attributes["state"] = self._host_data.get("state", "unknown")
            attributes["mac"] = self._host_data.get("mac", "unknown")
            attributes["hostname"] = self._host_data.get("hostname", "unknown")
            attributes["os"] = self._host_data.get("os", {})
            attributes["uptime"] = self._host_data.get("uptime", {})
            attributes["vendor"] = self._host_data.get("vendor", "unknown")
            attributes["type"] = self._host_data.get("type", "unknown")
            attributes["last_seen"] = self._host_data.get("last_seen", "unknown")
        return attributes

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="Home Network Monitor",
            manufacturer="Jari Kaipio",
            model="Local Network Scanner",
            configuration_url=self.coordinator.config_entry.data.get("url", ""),
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def should_poll(self) -> bool:
        """Return True as updates are needed."""
        return True


class Port(HomeNetworkMonitorEntity, SensorEntity):
    """Sensor for individual port information."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        port_data: dict,
        ip_address: str = "unknown",
    ) -> None:
        """Initialize the port sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._port_data = port_data
        self._port_number = port_data.get("portid", "unknown")
        self._unique_id = f"{DOMAIN}_port_{ip_address}_{self._port_number}"
        self._ip_address = ip_address
        self._attr_unique_id = f"{DOMAIN}_port_{ip_address}_{self._port_number}"

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return self._unique_id

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        return self._port_data.get("state", "unknown")

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"Port {self._port_number} on {self._ip_address}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}
        if self._port_data:
            attributes["portid"] = self._port_number
            attributes["proto"] = self._port_data.get("proto", "unknown")
            attributes["state"] = self._port_data.get("state", "unknown")
        return attributes

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="Home Network Monitor",
            manufacturer="Jari Kaipio",
            model="Local Network Scanner",
            configuration_url=self.coordinator.config_entry.data.get("url", ""),
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def should_poll(self) -> bool:
        """Return True as updates are needed."""
        return True
