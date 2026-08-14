import argparse
import requests 
import os
from dotenv import load_dotenv

load_dotenv()
GEOCODING_API = os.getenv("GEOCODING_API")

parser = argparse.ArgumentParser(description="Displays the day weather summary")
parser.add_argument("--city", help="select the city to display the weather")

args = parser.parse_args()

url = "http://api.openweathermap.org/geo/1.0/direct?q=" + args.city + "&appid=" + GEOCODING_API
response = requests.get(url)

print(response.json())
print(args.city)