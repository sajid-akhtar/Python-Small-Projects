import datetime
import requests
import time
import smtplib

MYLAT = 52.229675
MYLONG = 21.012230
SMTPSERVER = "smtp.gmail.com"
PORT = 587
USERNAME = "xyz@gmail.com"
PASSWORD = "app-password"

# ------------------------------------------ Function - Get ISS Position ------------------------------ #


def isIssOverhead() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if MYLAT-5 <= iss_lat <= MYLAT+5 and MYLONG-5 <= iss_long <= MYLONG+5:
        return True
    return False

# ----------------------------------------- Function - Sunrise/Sunset ----------------------------------- #


def isNight() -> bool:
    parameters = {
        "lat": MYLAT,
        "lng": MYLONG,
        "formatted": 0
    }
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True
    return False

# ------------------------------------ Final Check ---------------------------------- #


while True:
    time.sleep(60)
    if isNight() and isIssOverhead():
        with smtplib.SMTP(SMTPSERVER, port=PORT) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(from_addr=USERNAME,
                                to_addrs=USERNAME,
                                msg="Subject: Look Up!\n\nThe International Space Station is passing on top of you!!")
