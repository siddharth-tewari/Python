import openmeteo_requests
from openmeteo_sdk.Variable import Variable
import requests_cache
import pandas as pd
from retry_requests import retry
from geopy.geocoders import Nominatim
 
loc = Nominatim(user_agent="GetLoc")

place = str(input("Enter the Name of the Place: "))
getLoc = loc.geocode(place)


openmeteo = openmeteo_requests.Client()
params = {
    "latitude": getLoc.latitude,
    "longitude": getLoc.longitude,
    "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
    "current": ["temperature_2m", "relative_humidity_2m"]
}

responses = openmeteo.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
response = responses[0]
print("Coordinates", response.Latitude(), "°N", response.Longitude(), "°E")
print("Elevation", response.Elevation(), "m asl")
print("Timezone", response.Timezone(), response.TimezoneAbbreviation())
print("Timezone difference to GMT+0", response.UtcOffsetSeconds(), "s")

current = response.Current()
current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
current_relative_humidity_2m = next(filter(lambda x: x.Variable() == Variable.relative_humidity and x.Altitude() == 2, current_variables))

print("Current time", current.Time())
print("Current temperature_2m", current_temperature_2m.Value())
print("Current relative_humidity_2m", current_relative_humidity_2m.Value())
