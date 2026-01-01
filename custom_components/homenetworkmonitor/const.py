"""Constants for homenetworkmonitor."""

from logging import Logger, getLogger

from homeassistant.components.sensor import SensorEntityDescription

LOGGER: Logger = getLogger(__package__)

DOMAIN = "homenetworkmonitor"
ATTRIBUTION = "Data provided by Home Network Monitor"
UPDATE_INTERVAL = "update_interval"
DEFAULT_SCAN_INTERVAL = 5  # in minutes

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
