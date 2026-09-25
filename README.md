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

Example output (real run):

```
Your public IP address: 163.61.226.145
Location: Multan, Pakistan at (30.1968, 71.4782)
```

The map is written to `user_location_map.html` next to this script and opened in
your default browser automatically. If you would rather open it later, comment
out the `webbrowser.open(...)` call in `create_map()`.

The `ip-api.com` response carries more than the script uses — region, postal
code, timezone and ISP are all available in `data` if you want to print them.

## Notes

- **IP-based geolocation is approximate.** It reports the location of your ISP's
  exit node, not your device. Expect city-level accuracy at best, and a large
  offset if you are on a VPN or proxy.
- Free `ip-api.com` requests are capped at roughly 45 requests per minute.
- `user_location_map.html` is written next to the script and is git-ignored, so
  your location never gets committed.

## Cross-platform fix

`folium` needs a `file://` URL, and on Windows `Path.as_uri()` is used to
produce a correctly escaped one. The usual `"file://" + path` trick breaks on
Windows, and it is worth seeing why — a real captured comparison:

```
ours:  file:///E:/programmimg_world/geolocation-system/user_location_map.html
old:   file://E:\programmimg_world\user_location_map.html
```

Parsed as URLs:

| | ours | old |
| --- | --- | --- |
| `netloc` (hostname) | `''` | `'E:\programmimg_world\user_location_map.html'` |
| `path` | `/E:/.../user_location_map.html` | `''` |

The old version makes the entire file path the URL's **hostname** and leaves the
path **empty**. There is no file to open, so the browser silently does nothing.

## Concepts demonstrated

- Public IP discovery and REST API integration
- JSON response parsing
- `pathlib` for platform-correct file paths
- Interactive map generation with Folium
- `try` / `except` for network and API failures, including API-level error payloads

## License

MIT
