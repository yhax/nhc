### Home Assistant NHC Storm Sensors

A lightweight, high-performance Home Assistant custom integration that automatically tracks tropical system data from the National Hurricane Center (NOAA). It dynamically provisions a master tracking state alongside 10 dedicated, event-driven tracking sensors for both the Atlantic and Eastern Pacific basins—all without cluttering your system with complex YAML blocks.

### Features

*   **Zero YAML Configuration**: Fully managed via the Home Assistant Devices & Services user interface.
*   **Unified Parent-Child Architecture**: Employs a single thread-safe async REST entity (`sensor.nhc_storm_data`) that safely caches NOAA data attributes, completely bypassing thread-blocking rejections.
*   **Dynamic Slot Provisioning**: Automatically loops and tracks 5 Atlantic (AT1–AT5) and 5 Eastern Pacific (EP1–EP5) concurrent tropical systems.
*   **Clean Event Synchronization**: Child sensors sleep on system boot and only evaluate using high-performance `async_track_state_change_event` hooks *after* the master payload safely updates.
*   **Complete Attribute Mapping**: Tracks name, classification, storm intensity (TD, TS, Cat 1–5), pressure, heading, movement speed, distance, coordinates, and link pathways for graphics and discussions.

* * *

### Installation

Download and install directly through [HACS (Home Assistant Community Store)](https://hacs.xyz/):

[![Open your Home Assistant instance and open the NHC Storm Sensors integration inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=unclvito&repository=nhc&category=integration)

### Step 1: Install via HACS (Custom Repository)

1.  Open your Home Assistant instance and navigate to **HACS** > **Integrations**.
2.  Click the three vertical dots in the top-right corner and select **Custom repositories**.
3.  Paste https://github.com/unclvito/nhc into the **Repository** box.
4.  Select **Integration** as the Category and click **Add**.
5.  Locate the newly added **NHC Storm Sensors** card, click **Download**, and let the system copy the assets to your device.

### Step 2: Reload and Activate via UI

1.  Go to **Developer Tools** > **YAML** and select **Restart Home Assistant**.
2.  Once the system finishes booting, navigate to **Settings** > **Devices & Services**.
3.  Click the blue **Add Integration** button in the bottom-right corner.
4.  Search for **NHC Storm Sensors**, click on it, and click **Submit**.

* * *

### Tracked Attributes Reference

Every generated storm sensor dynamically populates the following metadata parameters:

Attribute Name

Description / Example Value

`friendly_name`

Full display name (e.g., *Hurricane Beryl*)

`storm_name`

Name assigned by NOAA (e.g., *BERYL* or *UNNAMED*)

`classification`

Meteorological status (e.g., *Hurricane* or *Tropical Storm*)

`pressure`

Minimum central pressure converted to inches of mercury (*inHg*)

`intensity`

Wind velocity parameter output tracking core tier brackets

`max_winds`

Sustained top wind velocity calculated in miles per hour (*MPH*)

`heading`

Absolute trajectory bearing vector angle (*0°–360°*)

`heading_text`

Broad cardinal direction mapping orientation (*WNW*, *North East*)

`movement_speed`

Ongoing forward speed of the storm center

`distance`

Calculated mileage distance relative to your Home Assistant zone location

`latitude` / `longitude`

Exact geographical coordinate floating values

`forecast_discussion`

Direct URL link string to the official NOAA text review feed

`forecast_graphics`

Direct URL link string to the updated target cone graphic image

* * *

### Example Badges

Since I am located on the eastern US, I watch the Atlantic storms. I have the following in my header:
```
      - type: entity
        show_name: true
        show_state: true
        show_icon: true
        entity: sensor.atlantic_storm_1
        visibility:
          - condition: state
            entity: sensor.atlantic_storm_1
            state_not: unavailable
        name: Storm
        tap_action:
          action: url
          url_path: https://www.nhc.noaa.gov/graphics_at1.shtml
      - type: entity
        show_name: true
        show_state: true
        show_icon: true
        entity: sensor.atlantic_storm_2
        visibility:
          - condition: state
            entity: sensor.atlantic_storm_2
            state_not: unavailable
        name: Storm
        tap_action:
          action: url
          url_path: https://www.nhc.noaa.gov/graphics_at2.shtml
      - type: entity
        show_name: true
        show_state: true
        show_icon: true
        entity: sensor.atlantic_storm_3
        visibility:
          - condition: state
            entity: sensor.atlantic_storm_3
            state_not: unavailable
        name: Storm
        tap_action:
          action: url
          url_path: https://www.nhc.noaa.gov/graphics_at3.shtml
      - type: entity
        show_name: true
        show_state: true
        show_icon: true
        entity: sensor.atlantic_storm_4
        visibility:
          - condition: state
            entity: sensor.atlantic_storm_4
            state_not: unavailable
        name: Storm
        tap_action:
          action: url
          url_path: https://www.nhc.noaa.gov/graphics_at4.shtml
      - type: entity
        show_name: true
        show_state: true
        show_icon: true
        entity: sensor.atlantic_storm_5
        visibility:
          - condition: state
            entity: sensor.atlantic_storm_5
            state_not: unavailable
        tap_action:
          action: url
          url_path: https://www.nhc.noaa.gov/graphics_at5.shtml
        name: Storm
```
This will show a pill when a storm is active, like right now ;)

### Tuning Polling Frequencies

By default, the master rest component queries the NOAA server safely every **15 minutes** to prevent triggering firewall security rejections (`403 Forbidden`).

If you want to manually scale or adjust this schedule, open your `sensor.py` file and modify the `SCAN_INTERVAL` duration tracking token:

python

    # Change minutes parameter to match your desired schedule preference
    SCAN_INTERVAL = timedelta(minutes=15)
    

Use code with caution.

* * *

### License

Distributed under the GNU Public License v3.0. See `LICENSE` for more information.
