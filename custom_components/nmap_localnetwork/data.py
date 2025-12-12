"""Custom types for nmap_localnetwork."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import NMapLocalNetworkApiClient
    from .coordinator import NMapLocalNetworkDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

type NMapLocalNetworkConfigEntry = ConfigEntry[NMapLocalNetworkData]


@dataclass
class NMapLocalNetworkData:
    """Data for the NMapLocalNetwork integration."""

    client: NMapLocalNetworkApiClient
    coordinator: NMapLocalNetworkDataUpdateCoordinator
    integration: Integration
