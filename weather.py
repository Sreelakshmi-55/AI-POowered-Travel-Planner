import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):

    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "Weather data not available."

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"Temperature: {temp}°C, Condition: {desc}"