"""Sensor platform for HomeNetworkMonitor."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.core import callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from .const import DOMAIN
from .coordinator import HomeNetworkMonitorDataUpdateCoordinator

if TYPE_CHECKING:
    from datetime import datetime

    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

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
        icon="mdi:lan-connect",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_host",
        name="Nmap Host data",
        icon="mdi:lan-connect",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_postscript",
        name="Nmap postscript data",
        icon="mdi:security-network",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_runstats",
        name="Nmap runstats data",
        icon="mdi:information-outline",
    ),
    SensorEntityDescription(
        key="homenetworkmonitor_port",
        name="Nmap host port data",
        icon="mdi:server-plus-outline",
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

    # Kick off the first update immediately
    await coordinator.async_request_refresh()

    dynamic_entities: dict[
        str, CoordinatorEntity[HomeNetworkMonitorDataUpdateCoordinator]
    ] = {}

    @callback
    def async_update_dynamic_entities() -> None:
        if not coordinator.data:
            return

        entity_registry = er.async_get(hass)
        new_ids: set[str] = set()
        hosts_data = coordinator.data.get("host", [])
        host_list = (
            hosts_data.get("host", []) if isinstance(hosts_data, dict) else hosts_data
        )

        for host_data in host_list:
            host = Host(coordinator, ENTITY_DESCRIPTIONS[2], host_data)
            host_id = Host.make_unique_id(host.ip)
            entity_id = entity_registry.async_get_entity_id(
                domain="sensor",
                platform=DOMAIN,
                unique_id=host_id,
            )

            if entity_id:
                _LOGGER.debug(
                    "Entity with unique_id %s already exists as %s", host_id, entity_id
                )
            elif host_id not in dynamic_entities:
                new_ids.add(host_id)
                dynamic_entities[host_id] = host
                async_add_entities([dynamic_entities[host_id]])

            os_data = host_data.get("os")

            ports = os_data.get("portused") or [] if isinstance(os_data, dict) else []

            for port_data in ports:
                port = Port(
                    coordinator,
                    ENTITY_DESCRIPTIONS[5],
                    host_data,
                    port_data,
                )
                port_id = Port.make_unique_id(host.ip, port_data)
                entity_id = entity_registry.async_get_entity_id(
                    domain="sensor",
                    platform=DOMAIN,
                    unique_id=port_id,
                )

                if entity_id:
                    _LOGGER.debug(
                        "Entity with unique_id %s already exists as %s",
                        port_id,
                        entity_id,
                    )
                elif port_id not in dynamic_entities:
                    new_ids.add(port_id)
                    dynamic_entities[port_id] = port
                    async_add_entities([dynamic_entities[port_id]])

    entry.async_on_unload(coordinator.async_add_listener(async_update_dynamic_entities))
    # Add main sensors
    static_entities = []
    host_hint_data = coordinator.data.get("hosthint", {})
    static_entities.append(
        NmapHostsSensor(coordinator, ENTITY_DESCRIPTIONS[1], host_hint_data)
    )

    static_entities.append(NmapScanInfoSensor(coordinator, ENTITY_DESCRIPTIONS[0]))
    post_script_data = coordinator.data.get("postscript", {})
    static_entities.append(
        NmapPostScriptSensor(coordinator, ENTITY_DESCRIPTIONS[3], post_script_data)
    )
    runstats_data = coordinator.data.get("runstats", {})
    static_entities.append(
        NmapRunstatsSensor(coordinator, ENTITY_DESCRIPTIONS[4], runstats_data)
    )

    async_add_entities(static_entities)
    async_update_dynamic_entities()


class NmapRunstatsSensor(
    CoordinatorEntity[HomeNetworkMonitorDataUpdateCoordinator],
):
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
        self._state = "unknown"
        finished = self._runstats_data.get("finished", {})
        if finished:
            self._state = finished.get("exit", "unknown")

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update sensor data when the coordinator publishes a new payload."""
        _LOGGER.debug("Sensors %s _handle_coordinator_update called.", self.name)
        if self.coordinator.data is None:
            self._state = "unknown"
        else:
            self._runstats_data = self.coordinator.data.get("runstats", {})
        finished = self._runstats_data.get("finished", {})
        if finished:
            self._state = finished.get("exit", "unknown")
        self._attr_available = self._state is not None
        self.force_update = True
        # # Tell Home Assistant to refresh the UI with the new state
        self.async_write_ha_state()

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
    def state(self) -> str:
        """Return the state of the sensor."""
        return self._state

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


class NmapPostScriptSensor(
    CoordinatorEntity[HomeNetworkMonitorDataUpdateCoordinator],
):
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
        self._state = len(self._post_script_data)
        self._attr_unique_id = f"{DOMAIN}_{self.entity_description.key}"

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update sensor data when the coordinator publishes a new payload."""
        _LOGGER.debug("Sensors %s _handle_coordinator_update called.", self.name)
        if self.coordinator.data is None:
            self._state = "unknown"
        else:
            self._post_script_data = self.coordinator.data.get("postscript", {})
            if self._post_script_data:
                self._state = len(self._post_script_data)
            else:
                self._state = 0
        self._attr_available = self._state is not None
        self.force_update = True
        # # Tell Home Assistant to refresh the UI with the new state
        self.async_write_ha_state()

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
        if self._post_script_data is None:
            return 0
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


class NmapHostsSensor(
    CoordinatorEntity[HomeNetworkMonitorDataUpdateCoordinator],
):
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

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update sensor data when the coordinator publishes a new payload."""
        _LOGGER.debug("Sensors %s _handle_coordinator_update called.", self.name)
        if self.coordinator.data is None:
            self._state = "unknown"
        else:
            self._post_script_data = self.coordinator.data.get("hosthint", {})
            self._state = len(self._post_script_data)
        self._attr_available = self._state is not None
        self.force_update = True
        # # Tell Home Assistant to refresh the UI with the new state
        self.async_write_ha_state()

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


class NmapScanInfoSensor(
    CoordinatorEntity[HomeNetworkMonitorDataUpdateCoordinator],
):
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
        self._scan_info = self.coordinator.data.get("scaninfo", {})

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update sensor data when the coordinator publishes a new payload."""
        _LOGGER.debug("Sensors %s _handle_coordinator_update called.", self.name)
        if self.coordinator.data is None:
            self._state = "unknown"
        else:
            self._scan_info = self.coordinator.data.get("scaninfo", {})
            self._state = len(self._scan_info)
        self._attr_available = self._state is not None
        self.force_update = True
        # # Tell Home Assistant to refresh the UI with the new state
        self.async_write_ha_state()

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}

        if self._scan_info:
            attributes["scan_type"] = self._scan_info.get("type", "unknown")
            attributes["protocol"] = self._scan_info.get("protocol", "unknown")
            attributes["num_services"] = self._scan_info.get("numservices", "unknown")

        return attributes

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        result = "unknown"
        if self.coordinator.data is None:
            return result

        if len(self._scan_info) > 0:
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


class Host(
    CoordinatorEntity[HomeNetworkMonitorDataUpdateCoordinator],
):
    """The host sensor ."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        description: SensorEntityDescription,
        host_data: dict,
    ) -> None:
        """Initialize the sensor ."""
        super().__init__(coordinator)
        self._state = "up"
        self._ip = NmapParser.extract_ip(host_data)
        for host in self.coordinator.data.get("host", []):
            if NmapParser.extract_ip(host) == self._ip:
                self._state = host.get("status", {}).get("state", "unknown")
        self.entity_description = description
        self._attr_unique_id = self.make_unique_id(self._ip)
        self._attr_available = True
        self._host_data = host_data

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update host/port data when the coordinator publishes a new payload."""
        host = self.coordinator.host_map.get(self._ip)
        if host:
            self._host_data = host
            self._state = host.get("status", {}).get("state", "unknown")
            self._attr_available = self._state is not None
            self.force_update = True
            _LOGGER.debug("Host %s found from coordinator.data.", self._ip)
            # # Tell Home Assistant to refresh the UI with the new state
            self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        """Register the sensor with the coordinator and Home Assistant."""
        _LOGGER.debug("%s async_added_to_hass called", self.name)
        await super().async_added_to_hass()
        # Immediately write the state so that the UI is updated at least once.
        self.async_write_ha_state()

    @staticmethod
    def make_unique_id(ip: str) -> str:
        """Make unique id of the sensor ."""
        return f"{DOMAIN}_host_{ip}"

    @property
    def available(self) -> bool:
        """The available of the sensor ."""
        return self._attr_available

    @property
    def native_value(self) -> str:
        """Native value of the sensor ."""
        return self._state  # e.g., "up" or "down"

    @property
    def state(self) -> str:
        """The state of the sensor ."""
        return self._state

    @property
    def name(self) -> str:
        """The name of the sensor ."""
        return f"Host {self._ip}"

    @property
    def ip(self) -> str:
        """The ip of the host ."""
        return self._ip

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}
        if self._host_data:
            attributes["ip"] = self._ip
            attributes["status"] = self._host_data.get("status")
            attributes["mac"] = NmapParser.extract_mac(self._host_data)
            attributes["hostnames"] = self._host_data.get("hostnames")
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


class Port(
    CoordinatorEntity[HomeNetworkMonitorDataUpdateCoordinator],
):
    """The port used by the host ."""

    def __init__(
        self,
        coordinator: HomeNetworkMonitorDataUpdateCoordinator,
        description: SensorEntityDescription,
        host_data: dict,
        port_data: dict,
    ) -> None:
        """Intitialization of the sensor ."""
        super().__init__(coordinator)
        self.entity_description = description
        self._port_data = port_data
        self._state = None
        self._ip = NmapParser.extract_ip(host_data)

        self._port = port_data.get("portid")
        self._attr_unique_id = self.make_unique_id(self._ip, port_data)
        self._attr_available = True
        self._attr_extra_state_attributes = {}
        self._port_state = "unknown"
        for port in host_data.get("os", {}).get("portused", []):
            if port.get("portid") == self._port:
                self._port_state = port.get("state", "unknown")
        self._state = self._port_state

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update host / port data when the coordinator publishes a new payload."""
        # Convert the port status that the coordinator sent into the entity state.
        new_hostdata = self.coordinator.host_map.get(self._ip)

        if (
            new_hostdata
            and new_hostdata.get("os")
            and self._port in new_hostdata.get("os", {}).get("portused", [])
        ):
            self._port_data = new_hostdata.get("os", {}).get("portused", [])[self._port]
            _LOGGER.debug("%s found in _handle_coordinator_update", self.name)

        self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        """Register the sensor with the coordinator and Home Assistant."""
        _LOGGER.debug("%s async_added_to_hass called", self.name)
        await super().async_added_to_hass()
        # Immediately write the state so that the UI is updated at least once.
        self.async_write_ha_state()

    @staticmethod
    def make_unique_id(ip: str, port_data: dict) -> str:
        """Make unique id of the sensor ."""
        return f"{DOMAIN}_port_{ip}_{port_data.get('portid')}"

    @property
    def available(self) -> bool:
        """The available of the sensor ."""
        return self._port_state is not None

    @property
    def native_value(self) -> str | None:
        """Native value of the sensor ."""
        return self._state  # e.g., "up" or "down"

    @property
    def state(self) -> str | None:
        """The state of the sensor ."""
        return self._state

    @property
    def name(self) -> str:
        """The name of the sensor ."""
        return f"Port {self._port} on {self._ip}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}
        if self._port_data:
            attributes["port_id"] = self._port
            attributes["protocol"] = self._port_data.get("protocol")
            attributes["state"] = self._port_data.get("state")
            attributes["service"] = self._port_data.get("service")
            attributes["version"] = self._port_data.get("version")
            attributes["ip_address"] = self._ip
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


class NmapParser:
    """Helper class to parse nmap data."""

    @staticmethod
    def extract_ip(host_data: dict[str, Any]) -> str:
        """
        Return the IPv4 address of the host.

        Nmap returns a list under the key ``address``.  Each element in the
        list is a dictionary that contains the fields:

        * ``addr``      the actual address string
        * ``addrtype``  the type of address (e.g. ``ipv4``, ``mac`` …)
        * ``vendor``   vendor information (may be ``null``)
        The first element of the list is *not* guaranteed to be the IPv4
        address it could be the MAC address first, or it could contain
        other address types.  Therefore we must look for the dictionary
        whose ``addrtype`` is ``ipv4``.

        If no IPv4 address is found we fall back to the legacy key
        ``host_data["ip"]`` (used by earlier versions of this integration)
        or the literal string ``"unknown"``.

        Args:
            host_data: Dictionary returned by Nmap for a single host.

        Returns:
            The IPv4 address as a string, or ``"unknown"`` when it cannot
            be determined.

        """
        addresses = host_data.get("address", [])
        if isinstance(addresses, list):
            # Find the entry whose addrtype is ipv4
            for addr_dict in addresses:
                if isinstance(addr_dict, dict) and addr_dict.get("addrtype") == "ipv4":
                    return addr_dict.get("addr", "unknown")
        # Fallback to the legacy key that some older Nmap outputs use
        return "unknown"

    @staticmethod
    def extract_mac(host_data: dict[str, Any]) -> str:
        """Extract mc addres."""
        addresses = host_data.get("address", [])
        if isinstance(addresses, list):
            # Find the entry whose addrtype is ipv4
            for addr_dict in addresses:
                if isinstance(addr_dict, dict) and addr_dict.get("addrtype") == "mac":
                    return addr_dict.get("addr", "unknown")
        # Fallback to the legacy key that some older Nmap outputs use
        return "unknown"
