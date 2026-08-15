import argparse
import json
import requests 
import os
from colorama import Fore, init, Style
from unit_conversor import kelvin_to_celsius, kelvin_to_fahrenheit
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from jsonpath_ng import jsonpath, parse

init()
load_dotenv()
WEATHER_API = os.getenv("WEATHER_API")

parser = argparse.ArgumentParser(description="Displays the day weather summary")
parser.add_argument("--city", help="select the city to display the weather")
parser.add_argument("--unit", help="select the unity to display the temperatures")

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
print("Displaying informations for " + Style.BRIGHT + args.city + ":")
for match in matches:
    if(kelvin_to_celsius(match) > 25):
        if args.unit == "metric":
            print(Fore.RED + f"Temperature: {kelvin_to_celsius(match)} °C")
        elif args.unit == "imperial":
            print(Fore.RED + f"Temperature: {kelvin_to_fahrenheit(match)} °F")
    elif(kelvin_to_celsius(match) < 15):
        if args.unit == "metric":
            print(Fore.BLUE + f"Temperature: {kelvin_to_celsius(match)} °C")
        elif args.unit == "imperial":
            print(Fore.BLUE + f"Temperature: {kelvin_to_fahrenheit(match)} °F")
    else:
        if args.unit == "metric":
            print(f"Temperature: {kelvin_to_celsius(match)} °C")
        elif args.unit == "imperial":
            print(f"Temperature: {kelvin_to_fahrenheit(match)} °F")


temperature_sensation = parse("$.main.feels_like")
matches = [match.value for match in temperature_sensation.find(json_awnser_formatted)]
for match in matches:
    if(kelvin_to_celsius(match) > 25):
        if args.unit == "metric":
            print(Fore.RED + f"Thermal Sensation: {kelvin_to_celsius(match)} °C")
        elif args.unit == "imperial":
            print(Fore.RED + f"Thermal Sensation: {kelvin_to_fahrenheit(match)} °F")
    elif(kelvin_to_celsius(match) < 15):
        if args.unit == "metric":
            print(Fore.BLUE + f"Thermal Sensation: {kelvin_to_celsius(match)} °C")
        elif args.unit == "imperial":
            print(Fore.BLUE + f"Thermal Sensation: {kelvin_to_fahrenheit(match)} °F")
    else:
        if args.unit == "metric":
            print(f"Thermal Sensation: {kelvin_to_celsius(match)} °C")
        elif args.unit == "imperial":
            print(f"Thermal Sensation: {kelvin_to_fahrenheit(match)} °F")

weather_summary = parse("$.weather[*].description")
matches = [match.value for match in weather_summary.find(json_awnser_formatted)]
for match in matches:
    print(Fore.RESET +  Style.DIM + f"Weather description: {match}")