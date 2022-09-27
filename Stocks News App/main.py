import requests
import os


STOCK = "TSLA"  # Tesla
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
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
difference_percentage = round((difference / yesterday_closing_price) * 100)


if difference_percentage > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news = news_response.json()['articles'][0:4]
    print(
        f"Tesla 🔺 {difference_percentage}%\nHeadline: {news[0]['title']}\nBrief: {news[0]['description']}")
    print(
        f"Tesla 🔺 {difference_percentage}%\nHeadline: {news[1]['title']}\nBrief: {news[1]['description']}")
    print(
        f"Tesla 🔺 {difference_percentage}%\nHeadline: {news[2]['title']}\nBrief: {news[2]['description']}")
else:
    print(f"Tesla 🔴 {difference_percentage}%\n No news for today")
