'''For the google worksheet:
https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?usp=sharing

Nutritionix API Documentation:
https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
'''
import requests
from datetime import datetime
import os

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY"),
}

parameters = {
    "query": input("What excerise did you do: "),
    "gender": "female",  # Your gender
    "weight_kg": 50.0,
    "height_cm": 168,
    "age": 20,
}

response = requests.post(
    "https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
data = response.json()["exercises"]

today = datetime.now().strftime(r"%d/%m/%Y")
time_now = datetime.now().strftime(r"%H:%M:%S")

bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
}

for exercise in data:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(os.environ.get(
        "SHEET_ENDPOINT"), json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
