from dotenv import load_dotenv
import os
import requests

load_dotenv() # Load environment variables from .env file
api_key = os.getenv("openweather_api_key")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

print(get_weather("Dachau"))