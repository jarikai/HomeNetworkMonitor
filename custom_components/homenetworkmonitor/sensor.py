"""Sensor platform for HomeNetworkMonitor."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from homeassistant.core import callback
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from .const import DOMAIN, ENTITY_DESCRIPTIONS
from .coordinator import HomeNetworkMonitorDataUpdateCoordinator

if TYPE_CHECKING:
    from datetime import datetime

    from homeassistant.components.sensor import SensorEntityDescription
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .data import HomeNetworkMonitorConfigEntry

_LOGGER = logging.getLogger(__name__)


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
    # Add main sensors
    static_entities = []
    static_entities.append(NmapHostsSensor(coordinator, ENTITY_DESCRIPTIONS[1]))

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

    @property
    def native_value(self) -> str:
        """Return the native value for this sensor."""
        return self._state


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
            self._state = 0
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
    def native_value(self) -> int:
        """Return the native value for this sensor."""
        return self._state

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
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._attr_unique_id = f"{DOMAIN}_{self.entity_description.key}"

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update sensor data when the coordinator publishes a new payload."""
        _LOGGER.debug("Sensors %s _handle_coordinator_update called.", self.name)
        if self.coordinator.host_info_map is None:
            self._state = 0
        else:
            self._state = len(self.coordinator.host_info_map)

        self._attr_available = self._state is not None
        self.force_update = True
        # # Tell Home Assistant to refresh the UI with the new state
        self.async_write_ha_state()

    @property
    def extra_state_attributes(self) -> dict:
        """Expose the whole map and simple hoshint data as an attribute."""
        attributes = {}
        attributes["host_info_map"] = self.coordinator.host_info_map
        attributes["host_map"] = self.coordinator.host_map
        return attributes

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "Devices"

    @property
    def native_value(self) -> int:
        """Return the native value for this sensor."""
        return self._state

    @property
    def state(self) -> int | None:
        """Return the state of the sensor."""
        return len(self.coordinator.host_info_map)

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
            self._state = 0
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
            attributes["services"] = self._scan_info.get("services", "unknown")

        return attributes

    @property
    def state(self) -> int:
        """Return the state of the sensor."""
        result = 0
        if self.coordinator.data is None:
            return result

        if len(self._scan_info) > 0:
            result = len(self._scan_info)

        return result

    @property
    def native_value(self) -> int:
        """Return the native value for this sensor."""
        return self._state

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
