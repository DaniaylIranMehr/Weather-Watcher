import requests

def geocode_city(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "weather-bot-training/1.0"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()  # 200 -> Successful | 4XX & 5xx -> ERROR
        data = r.json()
        print(data)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}. The response was not processed.")
    except requests.exceptions.Timeout:
        print("Request timed out after 10 seconds. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred during the request: {e}")
    except ValueError as e:
        print(f"Failed to parse JSON. The response might be malformed: {e}")
