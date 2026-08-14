import argparse
import json
import requests 
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from jsonpath_ng import jsonpath, parse

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
json_awnser = json.dumps(response.json())
json_awnser_formatted = json.loads(json_awnser)

temperature = parse("$.main.temp")
matches = [match.value for match in temperature.find(json_awnser_formatted)]
print("Displaying informations for " + args.city +":\n")
for match in matches:
    print(f"Temperature: {match}")

print("\n")

temperature_sensation = parse("$.main.feels_like")
matches = [match.value for match in temperature_sensation.find(json_awnser_formatted)]
for match in matches:
    print(f"Temperature sensation: {match}")

print("\n")

weather_summary = parse("$.weather[*].description")
matches = [match.value for match in weather_summary.find(json_awnser_formatted)]
for match in matches:
    print(f"Weather description: {match}")