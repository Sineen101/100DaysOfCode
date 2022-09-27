import requests
import os
from twilio.rest import Client


STOCK = "TSLA"  # COMPANY STOCK
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": os.environ.get("STOCK_API_KEY")
}

news_params = {
    "qInTitle": "Tesla",  # COMPANY_NAME
    "apiKey": os.environ.get("NEWS_API_KEY")
}

stocks_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stocks_response.raise_for_status()
stocks = stocks_response.json()["Time Series (Daily)"]
yesterday_stock = list(stocks.items())[0]
yesterday_closing_price = float(yesterday_stock["4. close"])

day_before_yesterday_stock = list(stocks.items())[1]
day_before_yesterday_closing_price = float(
    day_before_yesterday_stock["4. close"])
difference = yesterday_closing_price - day_before_yesterday_closing_price
difference_percentage = round((difference / yesterday_closing_price) * 100)

if difference > 0:
    raise_in_stock = "🔺"
elif difference < 0:
    raise_in_stock = "🔻"


if abs(difference_percentage) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news = news_response.json()['articles'][0:4]
    formatted_news = [
        f"{STOCK}: {raise_in_stock}\nHeadline: {news['title']}. \n{news['description']}" for news in news]

    client = Client(os.environ.get("TWILIO_ACCOUNT_SID"),
                    os.environ.get("TWILIO_AUTH_TOKEN"))
    for news in formatted_news:
        message = client.messages.create(body=news, from_=os.environ.get(
            "TWILIO_PHONE_NUMBER"), to=os.environ.get("MY_PHONE_NUMBER"))
        print(message.status)
