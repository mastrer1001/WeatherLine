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

`python WeatherLine.py -q <city> [-k <api-key>] [-d <default-city>] [-u <unit>]`



### Options

- `-h` : Open the help function
- `-q <city>`: Query the weather for the specified city.
- `-k <api-key>`: Set your OpenWeatherMap API key.
- `-d <default-city>`: Set the default city for weather queries.
- `-u <unit>`: Set the preferred unit for temperature (metric, imperial, or standard). Default is metric.
You can also query the weather for a city and set that city as the default city with `-qd <city>`

### Examples

1. Query the weather for a specific city:
   

`python WeatherLine.py -q <city>`


2. Set your API key:

`python WeatherLine.py -k YOUR_API_KEY`



3. Set a default city for weather queries:

`python WeatherLine.py -d Paris`



4. Set the preferred temperature unit to imperial (Fahrenheit):

`python WeatherLine.py -u imperial`

other valid units are 'metric' and 'standart' (Kelvin). 

## Making the Program executeable without using 'python' or '.py'

### Create an Executable Script:

Create an executable script that serves as the entry point to your program. This script should be placed in a directory that is included in your system's PATH. This allows you to run your program by simply typing its name in the terminal.

Create a new file, let's call it weatherLine, and make it executable:

`touch weatherLine`
`chmod +x weatherLine`

### Edit the Script:

Open the weather script in a text editor and define how it should execute your Python program. You should call your Python script with the appropriate interpreter (usually python) and pass any command-line arguments as needed.

Here's an example of what the weather script might look like:


`#!/bin/bash`

`python /path/to/your/weatherLine.py "$@"`

In this example, replace /path/to/your/weatherLine.py with the actual path to your Python script. The "$@" allows you to pass all the command-line arguments directly to your Python script.

### Move the Script to a Directory in Your PATH:

To be able to run the script from any location in your terminal, move it to a directory that is included in your system's PATH. Common directories for user scripts include /usr/local/bin or ~/bin. You may need root (administrator) privileges to move it to some directories.

For example, to move the script to /usr/local/bin, use:

`sudo mv weather /usr/local/bin`

Now, you should be able to run your weather command from the terminal:

`weatherLine -q Berlin`