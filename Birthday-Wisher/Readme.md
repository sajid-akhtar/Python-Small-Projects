########################## Simple Email App #####################

Modules Used:
    - smtplib
    - pandas
    - datetime
    - random
    - sys

Description:
    - Allows you to send email to a specific person by querying from the csv file
    - The email will be send only if the day and month matches with today's date
    - In code, allow your relative path where you will be putting all your files accordingly

How to configure your gmail to send email?
    - Go to https://myaccount.google.com/
    - Select Security on the left and scroll down to How you sign in to Google.
    - Enable 2-Step Verification
    - Click on 2-Step Verification again, and scroll to the bottom.
    - There you can add an App password.
    - Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.
    - COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
    - Use this App password in your Python code instead of your normal password.