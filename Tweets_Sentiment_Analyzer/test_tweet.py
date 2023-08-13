import unittest
from Tweets_Analyzer import TwitterSentimentAnalyzer as BaseTwitterSentimentAnalyzer
import tweepy

api_key = ".."
api_secret = ".."
access_token = ".."
access_token_secret = ".."

class TwitterSentimentAnalyzer(BaseTwitterSentimentAnalyzer):
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

class TestTwitterSentimentAnalyzer(unittest.TestCase):
    def test_search_tweets(self):
        analyzer = TwitterSentimentAnalyzer(api_key, api_secret, access_token, access_token_secret)
        results = analyzer.analyze("test query")
        assert isinstance(results, dict)
        assert "positive" in results
        assert "negative" in results
        assert "neutral" in results

if __name__ == '__main__':
    unittest.main()
