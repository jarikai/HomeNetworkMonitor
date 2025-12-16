"""Custom types for homenetworkmonitor."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import HomeNetworkMonitorApiClient
    from .coordinator import HomeNetworkMonitorDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

type HomeNetworkMonitorConfigEntry = ConfigEntry[HomeNetworkMonitorData]


@dataclass
class HomeNetworkMonitorData:
    """Data for the HomeNetworkMonitor integration."""

    client: HomeNetworkMonitorApiClient
    coordinator: HomeNetworkMonitorDataUpdateCoordinator
    integration: Integration
