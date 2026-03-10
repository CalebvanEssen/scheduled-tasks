import os
import requests
from twilio.rest import Client

#Open weather information
MY_LAT = 52.090736
MY_LONG = 5.121420
API_KEY = os.environ.get("OWM_API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/forecast"

#Twilio information
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_parameters = {
    'lat': 52.090736,
    'lon': 5.121420,
    'appid': API_KEY,
    'cnt': 4
}

response = requests.get(API_URL, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages.create(
        from_="whatsapp:+14155238886",
        body = "It's going to rain today. Be sure to bring an umbrella! ☔️",
        to="whatsapp:+64211776119"
    )

print(message.body)
