import requests

# API base URL and endpoint
api_key = "649597c47fd13799b12cd57e0046f0d8"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# City for which you want the weather
city = "Nairobi"

# Check also on this syntax:
api_url = f"https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api_key}"

# Request parameters
params = {
    "q": city,
    "appid": api_key,
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
