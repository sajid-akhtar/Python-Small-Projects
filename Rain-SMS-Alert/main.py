import requests
from twilio.rest import Client
import os

# ------------------------------------ Open Weather Data -------------------------------- #
openWeatherUrl = "https://api.openweathermap.org/data/2.5/forecast"
queryParams = {
    "lat": 52.229675,
    "lon": 21.012230,
    "appid": os.environ.get("OWA_API_KEY"),
    "cnt": 4
}

# ------------------------------------- Twilio Data ------------------------------------- #
account_sid = os.environ.get("T_ACCN_SID")
auth_token = os.environ.get("T_ATH_TKN")
twilio_my_phone_no = os.environ.get("T_PHN_NO")
client = Client(account_sid, auth_token)


# ----------------------------------------- Query Open Weather API ------------------------- #
try:
    response = requests.get(
        url=openWeatherUrl,
        params=queryParams
    )

    print(response.status_code)

except BaseException as e:
    print(e)
    print("Could not connect with the Open Weather API")

weatherData = response.json()
willRain = False

for hourData in weatherData["list"]:
    conditionCode = hourData["weather"][0]["id"]

    if int(conditionCode) < 700:
        willRain = True
        break

# -------------------------------------- Twilio SMS Alert -------------------------------------- #
if willRain:
    message = client.messages.create(
        body="It will rain. Please dont forget to take your umbrella.",
        from_=twilio_my_phone_no,
        to=os.environ.get("MY_PHN_NO")
    )

print(f"Sent Message Output: {message.status}")
