from twilio.rest import Client
import sys
from jproperties import Properties

# ------------------------------------------- Read Properties File --------------------------------------- #

data_file = Properties()
try:
    with open("D:\Python\Python-Small-Projects\Flight-Deal-Tracker\data.properties", "rb") as config_file:
        data_file.load(config_file)
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

TWILIO_SID = data_file.get("TWILIO_SID").data
TWILIO_AUTH_TOKEN = data_file.get("TWILIO_AUTH_TOKEN").data
TWILIO_VIRTUAL_NUMBER = data_file.get("TWILIO_VIRTUAL_NUMBER").data
TWILIO_VERIFIED_NUMBER = data_file.get("TWILIO_VERIFIED_NUMBER").data


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
