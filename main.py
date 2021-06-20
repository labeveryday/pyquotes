import os
from app.zen import ZenQuotes
from app.tweet import iTweet


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_KEY = os.environ["ACCESS_KEY"] 
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

def main():
    api = iTweet(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    quote = ZenQuotes()
    todays_quote = quote.today()
    api.send_tweet(f"{todays_quote['quote']}\n-- {todays_quote['author']}")

if __name__ == "__main__":
    main()
