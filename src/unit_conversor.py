def kelvin_to_celsius(temperature):
    celsius = temperature - 273.15
    return round(celsius,1)


def kelvin_to_fahrenheit(temperature):
    fahrenheit = ((temperature - 273.15) * 9)/5 + 32
    return round(fahrenheit, 1)

