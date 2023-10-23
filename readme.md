# Weather Query Program

The Weather Query Program is a command-line tool that allows you to retrieve current weather information for a specified city using the OpenWeatherMap API. It also provides options to set a default city, API key, and preferred unit for weather queries.

## Features

- Query the current weather for a specific city.
- Set or update your OpenWeatherMap API key.
- Specify a default city for weather queries.
- Set the preferred unit for temperature (metric, imperial, or standard).

## Prerequisites

Before using the Weather Query Program, you need to obtain an OpenWeatherMap API key. You can sign up for a free API key on the [OpenWeatherMap website](https://openweathermap.org/api).

## Usage

To use the Weather Query Program, open a command-line terminal and run the program with the following options:

python weather.py -q <city> [-k <api-key>] [-d <default-city>] [-u <unit>]



### Options

- `-h` : Open the help function
- `-q <city>`: Query the weather for the specified city.
- `-k <api-key>`: Set your OpenWeatherMap API key.
- `-d <default-city>`: Set the default city for weather queries.
- `-u <unit>`: Set the preferred unit for temperature (metric, imperial, or standard). Default is metric.

### Examples

1. Query the weather for a specific city:
   

python weather.py -q Berlin


2. Set your API key:

python weather.py -k YOUR_API_KEY



3. Set a default city for weather queries:

python weather.py -d Paris



4. Set the preferred temperature unit to imperial (Fahrenheit):

python weather.py -u imperial

other valid units are 'metric' and 'standart' (Kelvin). 

