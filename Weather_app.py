import requests

def get_weather(city_name):
    #  Yahan apni OpenWeatherMap API key daalo
    api_key = "YOUR-API-KEY"

    # Base URL for the API
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters to send to the API
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Celsius
    }

    # Request API
    response = requests.get(base_url, params=params)

    # Agar request sahi gai
    if response.status_code == 200:
        data = response.json()
        print("\n Current Weather Report ")
        print(f"City: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("\n Error: Unable to fetch weather data.")
        print("Check city name or API key!")

if __name__ == "__main__":
    print("=== CLI Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)