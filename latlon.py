from geopy.geocoders import Nominatim
from geopy.distance import distance
from geopy.exc import GeocoderTimedOut
import googlemaps
from timezonefinder import TimezoneFinder

import pandas as pd, numpy as np, io, urllib, pdb


def address_to_latlong(address):
    # Find lat, lon coordinates of given address                                
    # See https://www.openstreetmap.org/copyright for required copyright        
    # information using OSM service.  No more than 1 query per second!          
    # Try the free way first, then Google if OSM didn't find address            
    geolocator = Nominatim(user_agent="Trane Optics")
    try:
        location = geolocator.geocode(address)
        if location is not None:
            return location.latitude, location.longitude
    except GeocoderTimedOut:  pass
    # Try Google                                                                
    gmaps = googlemaps.Client(key='#fill in your own', timeout=2, retry_over_query_limit=False)
    # Choose first returned result                                              
    loc_return = gmaps.geocode(address)
    location = loc_return[0]['geometry']['location']

    return location['lat'], location['lng']


df = pd.read_excel('Efficient All-Electric Buildings in WA.xlsx',skiprows=1)

lats = []
longs = []

for index, row in df.iterrows():
    addr = row['All-Electric Building Name or Address']+' '+row['City']+' WA'
    lat, lon = address_to_latlong(addr)
    print(row['All-Electric Building Name or Address']
    lats.append(lat)
    longs.append(lon)

df['lat']=lats
df['lon']=longs

df.to_excel('eBuildings.xlsx')
