"""Constants for homenetworkmonitor."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "homenetworkmonitor"
ATTRIBUTION = "Data provided by Home Network Monitor"
UPDATE_INTERVAL = "update_interval"
DEFAULT_SCAN_INTERVAL = 5  # in minutes
