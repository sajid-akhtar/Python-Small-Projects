import requests
import sys
from jproperties import Properties
from datetime import date
from datetime import timedelta
from twilio.rest import Client
from requests.utils import DEFAULT_CA_BUNDLE_PATH

# ------------------------------------------- Read Properties File --------------------------------------- #

data_file = Properties()
try:
    with open("D:\Python\Python-Small-Projects\Stock-Price-Alert-App\data.properties", "rb") as config_file:
        data_file.load(config_file)
except FileNotFoundError as e:
    print(e)
    sys.exit(1)


# ------------------------------------------- Twilio API --------------------------------------- #
def sendSMSAlert(newsList):
    account_sid = data_file.get("TWILIO_ACCNT_SID").data
    auth_token = data_file.get("TWILIO_AUTH_TOKEN").data
    twilio_my_phone_no = data_file.get("TWILIO_MY_PHN_NO").data
    twilio_receivers_no = data_file.get("TWILIO_RECEIVER_NO").data
    client = Client(account_sid, auth_token)

    bodyMessage = ""
    for i in range(0, len(newsList)):
        if bodyMessage != "":
            bodyMessage = bodyMessage + "; " + newsList[i]
        else:
            bodyMessage = bodyMessage + newsList[i]

    message = client.messages.create(
        body=f"Stock Price changed by more than 4%,\nHeadlines: {bodyMessage}",
        from_=twilio_my_phone_no,
        to=twilio_receivers_no
    )

    print(f"Sent Message Output: {message.status}")

# -------------------------------------------- News API -------------------------------------- #


def getNewsForStocks(url, company, apiKey):
    queryParams = {
        "q": company,
        "apiKey": apiKey
    }
    URL = url

    try:
        print(
            f"Fetching News for: {data_file.get('COMPANY_NAME').data}")
        response = requests.get(
            URL,
            params=queryParams,
            verify=DEFAULT_CA_BUNDLE_PATH
        )

        newsHeadlines = []

        if response.json()["totalResults"] >= 3:
            for i in range(0, 3):
                newsHeadlines.append(response.json()["articles"][i]["title"])
        else:
            for i in range(0, response.json()["totalResults"]):
                newsHeadlines.append(response.json()["articles"][i]["title"])
        return newsHeadlines
    except BaseException as e:
        print(e)
        print("Couldn't communicate with News API.")
        sys.exit(1)

# ------------------------------------------------- Stock API ---------------------------------------------- #


def main():
    queryParams = {
        "function": data_file.get("FUNCTION").data,
        "symbol": data_file.get("SYMBOL").data,
        "apikey": data_file.get("API_KEY_STOCK").data
    }

    URL = data_file.get("STOCK_API_URL").data

    try:
        print(
            f"Fetching Stock Prices for: {data_file.get('COMPANY_NAME').data}")
        response = requests.get(
            URL,
            params=queryParams,
            verify=DEFAULT_CA_BUNDLE_PATH
        )

    except BaseException as e:
        print(e)
        print("Couldn't communicate with Stock API.")
        sys.exit(1)
    today = date.today()
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)

    stock_price_yesterday = response.json(
    )["Time Series (Daily)"][f"{yesterday}"]["4. close"]
    stock_price_day_bef_yesterday = response.json(
    )["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"]

    stock_difference = float(stock_price_yesterday) - \
        float(stock_price_day_bef_yesterday)
    percentage_change = round(
        (stock_difference/float(stock_price_yesterday)) * 100, 2)

    print(abs(percentage_change))

    if abs(percentage_change) >= 4.00:
        newsHeadlines = getNewsForStocks(
            data_file.get("NEWS_API_URL").data,
            data_file.get("COMPANY").data,
            data_file.get("API_KEY_NEWS").data
        )

        if newsHeadlines:
            sendSMSAlert(
                newsHeadlines
            )
    else:
        print("No need for news.")


# Main Function call
main()
