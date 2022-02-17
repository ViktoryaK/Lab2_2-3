"""
This module creates a map of user's friends locations
"""

from functools import lru_cache
import folium
from geopy import ArcGIS
from geopy.geocoders import Nominatim


arcgis = ArcGIS(timeout=10)
nominatim = Nominatim(timeout=10, user_agent="justme")


def get_names_locations(js):
    names_locations = {}
    for user in js['users']:
        if len(user['location']) > 0:
            names_locations[user['screen_name']] = user['location']
    return names_locations


@lru_cache(maxsize=None)
def geocode(address):
    """
    This function turns the address into the location and returns its latitude and longitude.
    Can be used only with main.
    >>> geocode('Coventry,  West Midlands,  England')
    (52.40772367500006, -1.5068478819999314)
    """
    geocoders = [arcgis, nominatim]
    i = 0
    try:
        location = geocoders[i].geocode(address)
        if location is not None:
            return location.latitude, location.longitude
        i += 1
        location = geocoders[i].geocode(address)
        if location is not None:
            return location.latitude, location.longitude
    except Exception:
        return None


def map_creation(names_locations):
    for name in names_locations.keys():
        try:
            location = geocode(names_locations[name])
            names_locations[name] = location
        except ValueError:
            names_locations[name] = None
    new_names_locations = {}
    for name in names_locations.keys():
        if names_locations[name] is not None:
            new_names_locations[name] = names_locations[name]
    names_locations = new_names_locations
    ucu = [49.817581, 24.023767]
    new_map = folium.Map(location=ucu, zoom_start=7)
    fg = folium.FeatureGroup(name="Friends' locations")
    for name in names_locations:
        fg.add_child(folium.Marker(location=names_locations[name], popup=name, icon=folium.Icon(color='green')))
    new_map.add_child(fg)
    new_map.add_child(folium.LayerControl())
    new_map.save('templates/Friends.html')
    return names_locations
