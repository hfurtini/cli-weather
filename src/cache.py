import json
import os
from jsonpath_ng import parse
from colorama import init, Style
def create_city_cache(city, file_name="default.json"):
    data = {
        "city": city
    }
    json_data = json.dumps(data)
    if os.path.exists(file_name):
        os.remove("default.json")
        with open(file_name, "w") as file:
            file.write(json_data)
            file.close
    else:
        with open(file_name, "w") as file:
            file.write(json_data)
            file.close

def read_city_cache():
    init()
    with open("default.json", "r") as json_file:
        content = json.load(json_file)
        city = content['city']
        return city