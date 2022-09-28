import requests
import os
from datetime import datetime


# datetime(year, month, day) for specific date
today = datetime(year=2022, month=9, day=28)

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph01"

pixela_params = {
    "token": TOKEN,  # os.environ.get("PIXELA_TOKEN"),
    "username": USERNAME,  # os.environ.get("PIXELA_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": "graph01",
    "name": "Programming Graph",
    "unit": "hours",
    "type": "float",
    "color": "ichou",
    "timezone": "Asia/Karachi",
}

pixel_params = {
    "date": today.strftime(r"%Y%m%d"),
    "quantity": str(input("How many hours did you code today? ")),
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Post request to create a user account
# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(response.text)

# Post a graph
# response = requests.post(
#     url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

# POST request to create a pixel
response = requests.post(
    url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(response.text)


# Update Pixel
# response = requests.put(url=f"{PIXEL_ENDPOINT}/{today.strftime(r'%Y%m%d')}", json=pixel_params, headers=headers)
# print(response.text)

# Delete Pixel
# response = requests.delete(url=f"{PIXEL_ENDPOINT}/{today.strftime(r'%Y%m%d')}", headers=headers)
# print(response.text)
