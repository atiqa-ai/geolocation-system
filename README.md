# Geolocation System

Fetches your approximate location from your public IP address and plots it on an
interactive [Folium](https://python-visualization.github.io/folium/) map.

Uses two free, key-less APIs:

1. [`api.ipify.org`](https://api.ipify.org) — discovers the public IP address
2. [`ip-api.com`](http://ip-api.com) — resolves that IP to coordinates

## Requirements

Python 3.7+ and an internet connection.

## Installation

```bash
git clone https://github.com/<your-username>/geolocation-system.git
cd geolocation-system

pip install -r requirements.txt
```

## Usage

```bash
python geolocation.py
```

Example output:

```
Your IP address: 203.0.113.42

Location Details:
  City     : Islamabad
  Region   : Islamabad Capital Territory
  Country  : Pakistan
  Zip      : 44000
  Latitude : 33.6844
  Longitude: 73.0479
  Timezone : Asia/Karachi

Map saved to: user_location_map.html
Open this file in a browser to see the map.
```

The generated map opens in your default browser automatically. If you would
rather just open the file later, comment out the `webbrowser.open(...)` call.

## Notes

- **IP-based geolocation is approximate.** It reports the location of your ISP's
  exit node, not your device. Expect city-level accuracy at best, and a large
  offset if you are on a VPN or proxy.
- Free `ip-api.com` requests are capped at roughly 45 requests per minute.
- `user_location_map.html` is written next to the script and is git-ignored, so
  your location never gets committed.

## Cross-platform fix

`folium` needs a `file://` URL, and on Windows `Path.as_uri()` is used to
produce a correctly escaped one. Building the path by hand — the usual
`"file://" + path` trick — breaks on Windows because the drive letter needs a
leading slash and backslashes are invalid in a URL.

## Concepts demonstrated

- Public IP discovery and REST API integration
- JSON response parsing
- `pathlib` for platform-correct file paths
- Interactive map generation with Folium
- `try` / `except` for network and API failures, including API-level error payloads

## License

MIT
