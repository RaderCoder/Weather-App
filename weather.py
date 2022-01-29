import requests

API_KEY = "your_api_key"
BASE_URL ="http://api.openweathermap.org/data/2.5/weather"

city=input("Enter a city name: ")
requests_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather=data['weather'][0]['description']
    temperature=round(data["main"]["temp"] - 273.15,2)
    print(f'Weather: {weather}')
    print(f'Temperature: {temperature}')
else:
    print("error")
