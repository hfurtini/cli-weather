import argparse
import json
import requests 
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
import time
from pprint import pprint

load_dotenv()
WEATHER_API = os.getenv("WEATHER_API")

parser = argparse.ArgumentParser(description="Displays the day weather summary")
parser.add_argument("--city", help="select the city to display the weather")

args = parser.parse_args()

app = Nominatim(user_agent="coordinates")
location = app.geocode(args.city).raw
latitude = location["lat"]
longitude = location["lon"]

url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API}"
response = requests.get(url)
json_awnser = response.json()
print(json_awnser)