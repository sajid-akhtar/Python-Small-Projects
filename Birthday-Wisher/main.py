import smtplib
import random
import datetime as dt
import pandas
import sys

MYEMAIL = "<Type-Your-Email>"
MYPASSWORD = "<Type-Your-App-Password-For-Your-Email>"
SMTPGMAIL = "<Type-Your-SMTP>"
SMTPPORT = 587
LETTERS = ["D:/Python/python/Birthday-Wisher/letter_templates/letter_1.txt",
           "D:/Python/python/Birthday-Wisher/letter_templates/letter_2.txt", "D:/Python/python/Birthday-Wisher/letter_templates/letter_3.txt"]

# ------------------------------ Send Email Function ----------------------------------------- #


def sendBirthdayWish(name, email):
    templatePath = random.choice(LETTERS)
    try:
        with open(templatePath) as file:
            message = file.read()
            messageBody = message.replace("[NAME]", name)
    except:
        print("Error. Exiting!")
        sys.exit(1)
    try:
        with smtplib.SMTP(SMTPGMAIL, port=SMTPPORT) as connection:
            connection.starttls()
            connection.login(user=MYEMAIL, password=MYPASSWORD)
            connection.sendmail(from_addr=MYEMAIL,
                                to_addrs=email, msg=f"Subject: Happy Birthday!\n\n{messageBody}")
    except:
        print("Error Sending Mail")
        sys.exit(1)

# -------------------------------- Read CSV Files for Date of Births ------------------------- #


try:
    data = pandas.read_csv("D:/Python/python/Birthday-Wisher/birthdays.csv")
except FileNotFoundError:
    print("File doesn't exist.")
    sys.exit(1)

data_dict = data.to_dict(orient="records")

# -------------------------------- Check for dates with today date ---------------------------- #

today = dt.datetime.now()
today_month = today.month
today_day = today.day

# ------------------------------- Check today's date and send email if true ------------------- #

for entry in data_dict:
    if entry["day"] == today_day and entry["month"] == today_month:
        sendBirthdayWish(entry["name"], entry["email"])
