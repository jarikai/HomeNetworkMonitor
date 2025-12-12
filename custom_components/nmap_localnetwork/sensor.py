"""Sensor platform for nmap_localnetwork."""

from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, LOGGER
from .coordinator import NMapLocalNetworkDataUpdateCoordinator
from .entity import NMapLocalNetworkEntity

if TYPE_CHECKING:
    import datetime

    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .data import NMapLocalNetworkConfigEntry

_LOGGER = logging.getLogger(__name__)

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="total_hosts",
        name="Nmap Total Hosts",
        icon="mdi:counter",
    ),
    SensorEntityDescription(
        key="scan_time",
        name="Nmap Scan Time",
        icon="mdi:timer",
    ),
    SensorEntityDescription(
        key="host",
        name="Nmap Host info",
        icon="mdi:computer-network",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: NMapLocalNetworkConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    # Create coordinator if not already created
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
    if entry.entry_id not in hass.data[DOMAIN]:
        # Initialize the coordinator here if needed
        coordinator = NMapLocalNetworkDataUpdateCoordinator(
            hass=hass,
            logger=LOGGER,
            name=DOMAIN,
            update_interval=None,
        )
        hass.data[DOMAIN][entry.entry_id] = coordinator
    else:
        coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    # Add the main sensors
    entities.append(NmapTotalHostsSensor(coordinator, ENTITY_DESCRIPTIONS[0]))
    entities.append(NmapScanTimeSensor(coordinator, ENTITY_DESCRIPTIONS[1]))

    # Add individual host sensors if data is available
    if coordinator.data and "hosts" in coordinator.data:
        seen_unique_ids = set()
        for host_data in coordinator.data["hosts"]:
            host_entity = Host(coordinator, ENTITY_DESCRIPTIONS[2], host_data)
            if host_entity.unique_id not in seen_unique_ids:
                entities.append(host_entity)
                seen_unique_ids.add(host_entity.unique_id)
            else:
                _LOGGER.debug(
                    "Skipping duplicate host entity with unique_id: %s",
                    host_entity.unique_id,
                )

    async_add_entities(entities, update_before_add=True)


class NmapScanTimeSensor(NMapLocalNetworkEntity, SensorEntity):
    """Sensor for Nmap scan time."""

    def __init__(
        self,
        coordinator: NMapLocalNetworkDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def state(self) -> datetime.datetime | str:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return "Unknown"
        scan_time = self.coordinator.data.get("scan_time")
        return scan_time if scan_time else "Unknown"

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"nmap_{self.entity_description.key}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.coordinator.config_entry.entry_id)
            },
            name="Nmap Local Network Scanner",
            manufacturer="jari@kaipio.com",
            model="Local Network Scanner",
        )


class NmapTotalHostsSensor(NMapLocalNetworkEntity, SensorEntity):
    """Sensor for Nmap total hosts."""

    def __init__(
        self,
        coordinator: NMapLocalNetworkDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def state(self) -> int:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return 0
        return self.coordinator.data.get("total_hosts", 0)

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"nmap_{self.entity_description.key}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.coordinator.config_entry.entry_id)
            },
            name="Nmap Local Network Scanner",
            manufacturer="jari@kaipio.com",
            model="Local Network Scanner",
        )


class Host(NMapLocalNetworkEntity, SensorEntity):
    """Sensor for individual host information."""

    def __init__(
        self,
        coordinator: NMapLocalNetworkDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        host_data: dict,
    ) -> None:
        """Initialize the host sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._host_data = host_data
        self._ip = host_data.get("ip", "unknown")
        self._unique_id = f"nmap_host_{self._ip}"

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return self._unique_id

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        return self._host_data.get("status", "unknown")

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"Nmap Host {self._ip}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}
        if self._host_data:
            attributes["ip"] = self._ip
            attributes["status"] = self._host_data.get("status")
            attributes["mac"] = self._host_data.get("mac")
            attributes["hostname"] = self._host_data.get("hostname")
            attributes["ports"] = self._host_data.get("ports", [])
        return attributes

    @property
    def ports(self) -> dict[str, str]:
        """Return the ports associated with the host."""
        return self._host_data["ports"]

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.coordinator.config_entry.entry_id)
            },
            name="Nmap Local Network Scanner",
            manufacturer="jari@kaipio.com",
            model="Local Network Scanner",
        )


class Port(NMapLocalNetworkEntity, SensorEntity):
    """Sensor for individual port information."""

    def __init__(
        self,
        coordinator: NMapLocalNetworkDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        port_data: dict,
        ip_address: str = "unknown",
    ) -> None:
        """Initialize the port sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._port_data = port_data
        self._port_number = port_data.get("port_id", "unknown")
        self._unique_id = f"nmap_port_{ip_address}_{uuid.uuid4()!s}"
        self._ip_address = ip_address

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
        return f"Nmap Port {self._port_number} on {self._ip_address}"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return the state attributes."""
        attributes = {}
        if self._port_data:
            attributes["port_id"] = self._port_number
            attributes["protocol"] = self._port_data.get("protocol")
            attributes["state"] = self._port_data.get("state")
            attributes["service"] = self._port_data.get("service")
            attributes["version"] = self._port_data.get("version")
            attributes["ip_address"] = self._ip_address
        return attributes

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.coordinator.config_entry.entry_id)
            },
            name="Nmap Local Network Scanner",
            manufacturer="jari@kaipio.com",
            model="Local Network Scanner",
        )
