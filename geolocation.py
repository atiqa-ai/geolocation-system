import requests
import folium
import webbrowser
import os
from pathlib import Path

# Function to get the user's public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None

# Function to get geolocation data from IP
def get_geolocation(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
        data = response.json()
        if data.get('status') == 'success':
            return {
                'lat': data['lat'],
                'lon': data['lon'],
                'city': data.get('city', 'Unknown'),
                'country': data.get('country', 'Unknown')
            }
        else:
            print("Failed to get geolocation data:", data.get('message', 'unknown error'))
            return None
    except requests.RequestException as e:
        print(f"Error fetching geolocation: {e}")
        return None

# Function to create and display a map
def create_map(lat, lon, city, country):
    # Create a map centered on the location
    m = folium.Map(location=[lat, lon], zoom_start=10)
    
    # Add a marker
    folium.Marker([lat, lon], popup=f"{city}, {country}").add_to(m)
    
    # Save the map as an HTML file next to this script
    map_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'user_location_map.html')
    m.save(map_file)
    
    # Open the map in the default web browser. Path.as_uri() builds a properly
    # encoded file:/// URL; a plain f"file://{path}" yields a malformed
    # "file://E:\..." string on Windows that the browser refuses to open.
    webbrowser.open(Path(map_file).resolve().as_uri())
    return map_file

# Main script
if __name__ == "__main__":
    ip = get_public_ip()
    if ip:
        print(f"Your public IP address: {ip}")
        location = get_geolocation(ip)
        if location:
            print(f"Location: {location['city']}, {location['country']} at ({location['lat']}, {location['lon']})")
            create_map(location['lat'], location['lon'], location['city'], location['country'])
        else:
            print("Could not retrieve location data.")
    else:
        print("Could not retrieve IP address.")
