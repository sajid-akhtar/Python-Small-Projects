import requests
from flightData import FlightData
import sys
from jproperties import Properties
from requests.utils import DEFAULT_CA_BUNDLE_PATH

# ------------------------------------------- Read Properties File --------------------------------------- #

data_file = Properties()
try:
    with open("D:\Python\Python-Small-Projects\Flight-Deal-Tracker\data.properties", "rb") as config_file:
        data_file.load(config_file)
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

# ----------------------------------------------- Class Flight Search ------------------------------------- #


class FlightSearch:
    def __init__(self) -> None:
        pass

    def flightSearch(self, destination_city_iata_code, from_time, to_time):
        kiwiUrl = data_file.get("KIWI_API").data
        kiwiApiKey = data_file.get("KIWI_API_KEY").data
        kiwiHeader = {
            "apikey": kiwiApiKey
        }
        kiwiQueryParams = {
            "fly_from": data_file.get("FLY_FROM").data,
            "fly_to": destination_city_iata_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "curr": data_file.get("CURRENCY").data,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0
        }
        try:
            responses = requests.get(
                url=kiwiUrl,
                headers=kiwiHeader,
                params=kiwiQueryParams,
                verify=DEFAULT_CA_BUNDLE_PATH
            )
        except BaseException as e:
            print(e)
            print("Cannot connect with Kiwi API.")
            sys.exit(1)

        try:
            flightDetails = responses.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_iata_code}.")
            return None

        flightData = FlightData(
            price=flightDetails["price"],
            origin_city=flightDetails["route"][0]["cityFrom"],
            origin_airport=flightDetails["route"][0]["flyFrom"],
            destination_city=flightDetails["route"][0]["cityTo"],
            destination_airport=flightDetails["route"][0]["flyTo"],
            out_date=flightDetails["route"][0]["local_departure"].split("T")[
                0],
            return_date=flightDetails["route"][1]["local_departure"].split("T")[
                0]
        )

        print(f"{flightData.destination_city}: PLN{flightData.price}")
        return flightData
