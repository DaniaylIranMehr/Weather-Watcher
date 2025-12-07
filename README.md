# Weather Notification Bot

This Python project fetches the current weather data for a specified city (Bologna, Italy) and sends it to a webhook endpoint. It demonstrates working with public APIs, JSON handling, and HTTP requests with authorization headers.

## Features

- Get latitude and longitude of a city using OpenStreetMap Nominatim API.
- Fetch current weather (temperature, wind speed, weather code) from Open-Meteo API.
- Send weather data as JSON to a webhook URL with a Bearer token.
- Designed for easy modification and integration.

# Usage

Edit main() in webhook.py to set your city, API key, and webhook URL:
city_name = "Bologna"
api_key = "test123"
webhook_url = "YOUR_WEBHOOK_URL"

The result will be displayed on the webhook server.

# Funcitons

## Returns the latitude and longitude of a city
def geocode_city(city):
    pass

## Fetches current weather data for given coordinates
def get_weather(lat, lon):
    pass

## Sends the weather data to the webhook
def send_to_webhook(data, webhook_url, api_key):
    pass
