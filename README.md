# Solax X1 Boost Inverter only integration.

[![Build Status](https://github.com/squishykid/solax/workflows/tests/badge.svg)](https://github.com/squishykid/solax/actions)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/solax.svg)](https://pypi.org/project/solax)

Read energy usage data from the real-time API on Solax solar inverters.

* Real time power, current and voltage
* Grid power information
* Battery level
* Temperature and inverter health
* Daily/Total energy summaries

# Home Assistant deployment as custom-component
- Delete any current Solax Integration aready added.
- Clone the repo in Home Assistant: 
    * cd config
    * cd custom_components
    * git clone https://github.com/japeral/solax
- Reboot HA.
- Add Solax integration, in the menu should be called now "SolaX Power: fixed to X1 Boost by Jose."
