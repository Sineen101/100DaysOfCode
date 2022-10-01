'''Google sheet link:
https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing

Google sheet API:
https://sheety.co/

Flight search API:
https://partners.kiwi.com/

Flight search API documentation:
https://tequila.kiwi.com/portal/docs/tequila_api

Twilio API:
https://www.twilio.com/docs/sms

IATA codes:
https://www.iata.org/publications/Pages/code-search.aspx
or
https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports
'''

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


for destination in sheet_data:
    flight = flight_search.check_flights(
        "PAK",
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only Rs.{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
