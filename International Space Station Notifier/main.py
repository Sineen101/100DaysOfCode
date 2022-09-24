import time
import requests
from datetime import datetime
import smtplib


current_location = {
    "lat": 34.006962,
    "lng": 71.533058,
    "formatted": 0,
}


def get_iss_location():
    """This function gets the location of the ISS from the Open Notify API."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return {
        "lat": iss_latitude,
        "lng": iss_longitude,
    }


def is_iss_overhead():
    """This function checks if the ISS is overhead."""
    iss_location = get_iss_location()
    iss_latitude = iss_location["lat"]
    iss_longitude = iss_location["lng"]
    if iss_latitude - 5 <= current_location["lat"] <= iss_latitude + 5 and iss_longitude - 5 <= current_location["lng"] <= iss_longitude + 5:
        return True


def is_night():
    """This function checks if it is night time."""
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=current_location)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)  # 60 seconds till the next check
    if is_iss_overhead() and is_night():  # If the ISS is overhead and it's night time
        with smtplib.SMTP("smtp.gmail.com") as connection:  # Connect to the SMTP server
            connection.ehlo()   # Identifies the client to the server.
            # Secure the connection. TLS(Transport Layer Security) is a cryptographic protocol that provides communication security over the Internet.
            connection.starttls()
            connection.ehlo()
            # Login to the email account
            connection.login(user="xxxx@gmail.com", password="xxxxxxxxxxxx")
            connection.sendmail(from_addr="xxxx@gmail.com", to_addrs="yyyyy@gmail.com",
                                msg="Subject:ISS is overhead\n\nLook up!")  # Send the email
