import sys
import requests
import json
from datetime import datetime

CONFIG_FILE = "config.json"

def get_default_unit():
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
            return config.get("default_unit")
    except FileNotFoundError:
        create_default_config()
        sys.exit(1)

def get_default_city():
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
            return config.get("default_city")
    except FileNotFoundError:
        create_default_config()
        sys.exit(1)

def get_api_key():
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
            return config.get("api_key")
    except FileNotFoundError:
        create_default_config()
        sys.exit(1)

def create_default_config():
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        config = {}

    if "api_key" not in config:
        config["api_key"] = "YOUR_INITIAL_API_KEY" # Set your desired API key here
    
    if "default_city" not in config:
        config["default_city"] = ""  # Set your desired default city here

    if "default_unit" not in config:
        config["default_unit"] = "standard"  # Set your desired default unit here

    with open(CONFIG_FILE, "w") as config_file:
        json.dump(config, config_file)

def update_default_city(default_city):
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        config = {}

    config["default_city"] = default_city

    with open(CONFIG_FILE, "w") as config_file:
        json.dump(config, config_file)

def update_default_unit(default_unit):
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        config = {}

    config["default_unit"] = default_unit

    with open(CONFIG_FILE, "w") as config_file:
        json.dump(config, config_file)

def update_api_key(api_key):
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        config = {}

    config["api_key"] = api_key

    with open(CONFIG_FILE, "w") as config_file:
        json.dump(config, config_file)

def filter_forecasts(data, days=4):
    filtered_forecasts = data['list'][::8][:days]
    return filtered_forecasts

def get_weather(city, api_key, unit="standard", days=4):
    base_url = 'https://api.openweathermap.org/data/2.5/forecast'

    params = {
        'q': city,
        'appid': api_key,
        'units': unit
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Define a dictionary to map units to symbols
    unit_symbols = {
        "imperial": "°F",
        "metric": "°C",
        "standard": "K"
    }

    if response.status_code == 200:
        print(f"Weather forecast for {city} for the next {days} days:")
        filtered_forecasts = filter_forecasts(data, days)

        for forecast in filtered_forecasts:
            timestamp = forecast['dt']
            date = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y %H:%M:%S')
            weather_description = forecast['weather'][0]['description']
            temperature = forecast['main']['temp']
            unit_symbol = unit_symbols.get(unit, '°C')
            print(f"Date: {date}")
            print(f"Weather: {weather_description.capitalize()}")
            print(f"Temperature: {temperature}{unit_symbol}")
            print("------")
    else:
        print(f"Failed to retrieve daily weather forecast for {city}")
        print(data)

if __name__ == "__main__":
    args = {}
    i = 1

    while i < len(sys.argv):
        if sys.argv[i] == "-h":
            print("Usage: python WeatherLine.py [-q <city>] [-k <api-key>] [-u <unit>] [-d <default-city>]")
            print("Options:")
            print("  -q <city>        Query the weather for the specified city.")
            print("  -k <api-key>     Set your OpenWeatherMap API key.")
            print("  -u <unit>        Set the preferred unit (metric, imperial, standard). Default is metric.")
            print("  -d <default-city> Set the default city for weather queries.")
            sys.exit(0)
        
        if sys.argv[i] in ["-q", "-k", "-u", "-d", "-qd"]:
            if i + 1 < len(sys.argv):
                args[sys.argv[i]] = sys.argv[i + 1]
                i += 2
            else:
                print(f"Please provide a value after '{sys.argv[i]}'.")
                sys.exit(1)
        else:
            print(f"Unrecognized option: {sys.argv[i]}")
            sys.exit(1)

    city = args.get("-q")
    api_key = args.get("-k")
    unit = args.get("-u")

    if api_key:
        update_api_key(api_key)

    if "-qd" in args:
        city = args["-qd"]
        update_default_city(city)

    if "-u" in args:
        update_default_unit(unit)
    
    if "-d" in args:
        default_city = args["-d"]
        update_default_city(default_city)

    if not city:
        city=get_default_city()

    if not api_key:
        api_key=get_api_key()
    
    if not unit:
        unit=get_default_unit()
    
    if city:
        get_weather(city, api_key, unit)
    else:
        print("Usage: python WeatherLine.py [-q <city>] [-k <api-key>] [-u <unit>] [-d <default-city>]")
        print("Options:")
        print("  -q <city>        Query the weather for the specified city.")
        print("  -k <api-key>     Set your OpenWeatherMap API key.")
        print("  -u <unit>        Set the preferred unit (metric, imperial, standard). Default is metric.")
        print("  -d <default-city> Set the default city for weather queries.")
