import requests
from twilio.rest import Client
import os


parameters = {
    "lat": 34.006962,   # Your latitude
    "lon": 71.533058,   # Your longitude
    "exclude": "current,minutely,daily",
    "appid": os.environ.get("API_KEY"),    # Your API Key
}

response = requests.get(
    url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][0:12]
condition_code = [hour_data["weather"][0]["id"] for hour_data in weather_data]

umberella_needed = False
for weather in condition_code:
    if weather < 700:
        umberella_needed = True

if umberella_needed:
    # Your Twilio SID and Auth Token emported as environment variables
    client = Client(os.environ.get("SID"), os.environ.get("AUTH_TOKEN"))
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an 🌂",
            from_='+15012311111',    # Your Twilio number
            to='+155343326324'       # Your verified number
        )
    print(message.status)

# use this link to get your API key: https://openweathermap.org/api/one-call-api
# use this link to get your Twilio account: https://www.twilio.com/
# use this link to get your Twilio number: https://www.twilio.com/console/phone-numbers/verified
# use this link to get your Twilio auth token: https://www.twilio.com/console
# use pythonanywhere.com to host your app
# use this link to get your pythonanywhere account: https://www.pythonanywhere.com/
# After creating your account, go to the dashboard and click on the "Bash" tab and type the following commands:
# pip3.6 install twilio. This will install the twilio module. You can also install other modules like requests, etc.
# pip3.6 freeze > requirements.txt. This will create a requirements.txt file which will contain all the modules you have installed.
# Now go to the "Web" tab and click on "Add a new web app". Select "Manual configuration" and then select "Python 3.6". Click on "Next".
# Now click on "Upload a zip file" and upload your project folder. Click on "Next".
# Now click on "Reload" and your app will be hosted on pythonanywhere.com
# Now go to the "Files" tab and click on "Upload a file". Upload your requirements.txt file. Click on "Next".


# If there's an exception raised, use this link for help: https://www.pythonanywhere.com/forums/topic/11506/
