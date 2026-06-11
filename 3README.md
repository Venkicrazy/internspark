# Weather Information App Using OpenWeather API

## Project Overview

The Weather Information App is a Python-based application that retrieves real-time weather information for any city using the OpenWeather API. Users can search for a city and view weather details such as temperature, humidity, weather conditions, and wind speed.

## Objectives

- Fetch real-time weather data from an online API.
- Parse JSON responses using Python.
- Display weather information in a user-friendly format.
- Allow users to search weather details for different cities.

## Features

- Search weather by city name
- Real-time weather information
- Temperature display in Celsius
- Humidity information
- Weather condition description
- Wind speed information
- Error handling for invalid city names
- Multiple city searches in a single session

## Technologies Used

- Python
- Requests Library
- OpenWeather API
- JSON Data Parsing

## Requirements

Install the required package:

```bash
pip install requests
```

## How to Run

1. Download the project files.
2. Install the requests library.
3. Create a free account on OpenWeather.
4. Generate an API key.
5. Replace the API key in the source code.
6. Open terminal in the project folder.
7. Run:

```bash
python weather_app.py
```

## Sample Output

```
================================
      WEATHER INFORMATION APP
================================

Enter City Name: Bangalore

Weather Details
----------------------------
City : Bengaluru
Country : IN
Temperature : 28°C
Humidity : 65%
Weather : scattered clouds
Wind Speed : 3.5 m/s
```

## Project Structure

```
Weather_API_Project
│
├── weather_app.py
├── README.md
```

## Learning Outcomes

- Working with REST APIs
- Using the Requests library
- Parsing JSON responses
- Exception handling
- User input handling
- Real-world API integration
