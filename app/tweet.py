"""
Script sends a tweet to your twitter TL.
Leverages the tweepy API: https://docs.tweepy.org/en/latest/api.html
Obtain API Keys: https://developer.twitter.com/
"""
import tweepy


class iTweet:
    def __init__(self, consumer_key, consumer_secret,
                 access_key, access_secret):
        """Initializes the iTweet class
            Args:
                consumer_key (str): Developer consumer key
                consumer_secret (str): Developer consumer secret
                access_key (str): Developer access key
                access_secret (str): Developer access secret
            return: Return the api class object
            rtype: class
        """
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_key = access_key
        self.access_secret = access_secret
        self.api = self.login()

    def login(self):
        """POST connects to Twitter and returns api handler
            Obtain API Keys: https://developer.twitter.com/
            Args:
                consumer_key (str): Developer consumer key
                consumer_secret (str): Developer consumer secret
                access_key (str): Developer access key
                access_secret (str): Developer access secret
            return: Return the api class object
            rtype: class
        """
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        return tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    def send_tweet(self, message):
        """POST Sends twitter message to user timeline
            Args:
                api_auth(class): Twitter api handler
                message (str): Tweet to user TL
            return: None
            rtype: dict
        """
        print('The user is %s' % user['name'])
        self.api.update_status(message)