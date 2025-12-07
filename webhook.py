import requests

def geocode_city(city):
    """
    Given a city name, return its latitude and longitude using OpenStreetMap Nominatim API.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "weather-bot-training/1.0"
    }
    
    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()  # 200 -> Successful | 4XX & 5xx -> ERROR
        data = r.json()

        if not data:
            print(f"No results found for city '{city}'.")
            return None

        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}. The response was not processed.")
    except requests.exceptions.Timeout:
        print("Request timed out after 10 seconds. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred during the request: {e}")
    except ValueError as e:
        print(f"Failed to parse JSON. The response might be malformed: {e}")


def get_weather(lat, lon):
    """
    Given latitude and longitude, fetch current weather data from Open-Meteo API.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather":True
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "current_weather" not in data:
                print("No current weather data available.")
                return None

        weather = data["current_weather"]
        temperature = weather.get("temperature")
        windspeed = weather.get("windspeed")
        weathercode = weather.get("weathercode")

        print(f"Weather data retrieved: Temperature={temperature}°C, Windspeed={windspeed} km/h, WeatherCode={weathercode}")
        return weather

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred while fetching weather: {e}")
    except requests.exceptions.Timeout:
        print("Weather request timed out after 10 seconds.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred during the weather request: {e}")
    except ValueError as e:
        print(f"Failed to parse JSON from weather API: {e}")


def send_to_webhook(data, webhook_url, api_key):
    """
    Send JSON data to a webhook URL with Authorization header.
    """
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    try:
        response = requests.post(webhook_url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        print("Data sent successfully!")
        print("HTTP status:", response.status_code)
        print("Response text (first 500 chars):", response.text[:500])
    except requests.exceptions.RequestException as e:
        print("Error sending to webhook:", e)



def main():
    city_name = "Bologna"
    api_key = "test123"
    webhook_url = "https://webhook.site/8546f6e9-3a57-406b-847e-8982b5e4cfec"

    coords = geocode_city(city_name)
    if coords is None:
        print("Could not get coordinates!")
        return

    lat, lon = coords
    print(f"Coordinates of {city_name}: Latitude={lat}, Longitude={lon}")

    weather = get_weather(lat, lon)
    if weather is None:
        print("Weatehr data not available!")
        return
    
    payload = {
        "city": city_name,
        "latitude": lat,
        "longitude": lon,
        "temperature": weather.get("temperature"),
        "windspeed": weather.get("windspeed"),
        "weathercode": weather.get("weathercode")
    }

    send_to_webhook(payload, webhook_url, api_key)


if __name__ == "__main__":
    main()