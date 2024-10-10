"""Constants for the solax_x1_boost integration."""

from solax import InverterResponse

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class SolaxDataUpdateCoordinator(DataUpdateCoordinator[InverterResponse]):
    """DataUpdateCoordinator for solax_x1_boost."""