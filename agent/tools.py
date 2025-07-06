import requests

def get_news(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey=YOUR_API_KEY"
    return requests.get(url).json()
