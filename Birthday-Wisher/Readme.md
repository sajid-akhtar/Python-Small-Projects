########################## Simple Email App #####################

Modules Used:<br/>
    - smtplib<br/>
    - pandas<br/>
    - datetime<br/>
    - random<br/>
    - sys<br/>

Description:<br/>
    - Allows you to send email to a specific person by querying from the csv file<br/>
    - The email will be send only if the day and month matches with today's date<br/>
    - In code, allow your relative path where you will be putting all your files accordingly<br/>

How to configure your gmail to send email?<br/>
    - Go to https://myaccount.google.com/<br/>
    - Select Security on the left and scroll down to How you sign in to Google<br/>
    - Enable 2-Step Verification<br/>
    - Click on 2-Step Verification again, and scroll to the bottom<br/>
    - There you can add an App password<br/>
    - Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate<br/>
    - COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces<br/>
    - Use this App password in your Python code instead of your normal password<br/>