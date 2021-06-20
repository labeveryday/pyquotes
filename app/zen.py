import requests
import sys


class ZenQuotes(object):

    def __init__(self, api_key=None):
        self.key = api_key
        self.url = "https://zenquotes.io/api/"

    def create_url(self, retreval_type, author_name=None):
        if retreval_type is "quotes":
            return self.url + "quotes" + "/" + self.key if self.key else self.url + "quotes"
        elif retreval_type is "author":
            return (self.url + f"quotes/author/{author_name}" + "/" +
                    self.key if self.key else self.url + f"quotes/author/{author_name}")
        elif retreval_type is "random":
            return self.url + "random" + "/" + self.key if self.key else self.url + "random"
        elif retreval_type is "today":
            return self.url + "today" + "/" + self.key if self.key else self.url + "today"
    
    def today(self):
        """
        Generate the quote of the day on each request
        """
        today_resp = {}
        url = self.create_url("today")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response_json = response.json()
                for key in response_json[0]:
                    if key == "q":
                        today_resp['quote'] = response_json[0][key]
                    elif key == "a":
                        today_resp['author'] = response_json[0][key]
            else:
                print("Unable to connect. Please verify connectivity to zenquotes.io")
        except Exception as err:
            print(err)
        return today_resp
    
    def random(self):
        """
        Generate a random quote on each request
        """
        random_resp = {}
        try:
            response = requests.get("https://zenquotes.io/api/random")
            if response.status_code == 200:
                response_json = response.json()
                for key in response_json[0]:
                    if key == "q":
                        random_resp['quote'] = response_json[0][key]
                    elif key == "a":
                        random_resp['author'] = response_json[0][key]
            else:
                print("Unable to connect. Please verify connectivity to zenquotes.io")
        except Exception as err:
            print(err)
        return random_resp
    
    def author(self, author):
        """
        Generate a Dict array of quotes from specific author (API Key Required)
        List of authors: https://premium.zenquotes.io/available-authors/
            Arguments:
                author (str): String name of author i.e. 'alan-watts'
            Returns: dict of author quotes
        """
        if not self.key:
            sys.exit("Failed: Unauthorized API request,"\
                     "key required. Visit zenquotes.io for documentation.")
        author_resp = {}
        url = self.create_url("author", author)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response_json = response.json()
                for key in response_json[0]:
                    if key == "q":
                        author_resp['quote'] = response_json[0][key]
                    elif key == "a":
                        author_resp['author'] = response_json[0][key]
            else:
                print("Unable to connect. Please verify connectivity to zenquotes.io")
        except Exception as err:
            print(err)
        return author_resp
    
    def quotes(self):
        """
        Generates a List array of 50 random quotes on each request
        """
        quotes_list = []
        url = self.create_url("quotes")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response_json = response.json()
                for item in response_json:
                    resp = {}
                    if item['q']:
                        resp['quote'] = item['q']
                    if item['a']:
                        resp['author'] = item['a']
                    quotes_list.append(resp)
        except Exception as err:
            print(err)
        return quotes_list
