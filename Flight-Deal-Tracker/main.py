import requests
import sys
from jproperties import Properties
from flightSearch import FlightSearch
from datetime import datetime, timedelta
from notificationManager import NotificationManager
from requests.utils import DEFAULT_CA_BUNDLE_PATH

# ------------------------------------------- Read Properties File --------------------------------------- #

data_file = Properties()
try:
    with open("D:\Python\Python-Small-Projects\Flight-Deal-Tracker\data.properties", "rb") as config_file:
        data_file.load(config_file)
except FileNotFoundError as e:
    print(e)
    sys.exit(1)


# --------------------------------------------- Reading Sheety API for Flight Details -------------------------------------- #


def main():
    sheetyUrl = data_file.get("SHEETY_URL").data
    sheetyApiToken = data_file.get("SHEETY_BASIC_AUTH_TOKEN").data

    sheetyHeader = {
        "Authorization": "Basic " + str(sheetyApiToken)
    }

    try:
        responses = requests.get(
            url=sheetyUrl,
            headers=sheetyHeader,
            verify=DEFAULT_CA_BUNDLE_PATH
        )
    except BaseException as e:
        print(e)
        print("Cannot connect with Sheety API.")
        sys.exit(1)

    googleSheetData = responses.json()["sheet1"]
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in googleSheetData:
        flight = flight_search.flightSearch(
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )

        # print(flight.price)
        # print(destination["lowestPrice"])

        if flight.price < destination["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only PLN{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )


main()
