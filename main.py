import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "6b17373125d0d342d6e49703319479d9"

weather_params = {
    "lat": 6.502750,
    "lon": 3.370530,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
else:
    print("Ain't gonna rain")
