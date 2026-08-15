from jsonpath_ng import parse
def add_emoji(description, json_awnser_formated):
    weather_icon = parse("$.weather[*].icon")
    matches = [match.value for match in weather_icon.find(json_awnser_formated)]
    for match in matches:
        weather_icon = match

    str(weather_icon)
    if(weather_icon[0:2] == "11"): print("🌧")
    elif(weather_icon[0:2] == "09d"): print("❄️")
    elif(weather_icon[0:2] == "10"): print("⛈")
    elif(weather_icon[0:2] == "01"): print("☀️")
    return
