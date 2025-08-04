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
![search for solax](https://private-user-images.githubusercontent.com/7840678/474013345-9100e2e8-47f1-42f5-a762-6cb82ffd70c0.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTQzMDg0NzUsIm5iZiI6MTc1NDMwODE3NSwicGF0aCI6Ii83ODQwNjc4LzQ3NDAxMzM0NS05MTAwZTJlOC00N2YxLTQyZjUtYTc2Mi02Y2I4MmZmZDcwYzAucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDgwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA4MDRUMTE0OTM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OTU3OTkyZTc3ZDRmNzUwY2I0MzhhNDUwOWJiZGM3ZTI4ODlmMDlmMGRjN2YxYWIyN2UzYWQwMDYxYjg3NjdiNiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.npi68aJQv9eayKJWMp-cbKJPHknK-jqwQvO3uBBzqAA)

![settings](https://private-user-images.githubusercontent.com/7840678/474010734-e3a65d99-8a05-431c-a5cc-f6534085b320.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTQzMDg0NzUsIm5iZiI6MTc1NDMwODE3NSwicGF0aCI6Ii83ODQwNjc4LzQ3NDAxMDczNC1lM2E2NWQ5OS04YTA1LTQzMWMtYTVjYy1mNjUzNDA4NWIzMjAucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDgwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA4MDRUMTE0OTM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODM0NzZjMDYzNjljNTc2MTJiMjg4ZWU3ZjEyZjQ0ZTQ2NWQ5YWMwNTFhOTUxMDQ2YWRmYjVjOTg3NWEyMjc0NiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.xXzZqXrQeraFmBMavcAUlFE8wSkLpz1DorOwB-jli14)