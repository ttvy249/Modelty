import requests


def get_coordinates(city_name, geocoding_api_key):
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        'q': city_name,
        'key': geocoding_api_key
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            lat = data['results'][0]['geometry']['lat']
            lng = data['results'][0]['geometry']['lng']
            return lat, lng
        else:
            print(f"Error: No results found for {city_name}")
            return None, None
    else:
        print(f"Error: Unable to fetch coordinates for {city_name}. HTTP Status code: {response.status_code}")
        return None, None


def get_weather(api_key, lat, lng):
    base_url = "https://api.stormglass.io/v2/weather/point"
    params = {
        'lat': lat,
        'lng': lng,
        'params': 'airTemperature,humidity'
    }
    headers = {
        'Authorization': api_key
    }
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        process_weather_data(data)
    else:
        print(f"Error: Unable to fetch weather data. HTTP Status code: {response.status_code}")


def process_weather_data(data):
    if 'hours' in data:
        latest_data = data['hours'][0]
        temperature = latest_data['airTemperature']['noaa']
        humidity = latest_data['humidity']['noaa']
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("No weather data available")


if __name__ == "__main__":
    city = input("Enter the city name: ")
    geocoding_api_key = "e1bf1dceb8604b7eac97b30e166de302"  # Thay thế bằng API key của OpenCage
    weather_api_key = "edfc7bc8-4397-11ef-968a-0242ac130004-edfc7c2c-4397-11ef-968a-0242ac130004"  # Thay thế bằng API key của StormGlass

    lat, lng = get_coordinates(city, geocoding_api_key)

    if lat is not None and lng is not None:
        get_weather(weather_api_key, lat, lng)
