import requests
import requests

# API base URL and endpoint
API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# City for which you want the weather
city = "Nairobi"

# Request parameters
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Temperature in Celsius
}

# Sending GET request
try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    data = response.json()  # Parse the JSON response

    # Extracting and displaying specific data
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"Current weather in {city}:")
    print(f"- Weather: {weather}")
    print(f"- Temperature: {temp}°C")
    print(f"- Humidity: {humidity}%")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
