import argparse
import unittest
from Tweets_Analyzer import TwitterSentimentAnalyzer as BaseTwitterSentimentAnalyzer
import tweepy

parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Your Twitter API key')
parser.add_argument('--ksecret', help='Your Twitter API secret key')
parser.add_argument('--token', help='Your Twitter access token')
parser.add_argument('--tsecret', help='Your Twitter access token secret')
args = parser.parse_args()

class TwitterSentimentAnalyzer(BaseTwitterSentimentAnalyzer):
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


class TestTwitterSentimentAnalyzer(unittest.TestCase):
    def test_search_tweets(self):
        analyzer = TwitterSentimentAnalyzer(args.key, args.ksecret, args.token, args.tsecret)
        results = analyzer.analyze("test query")
        assert isinstance(results, dict)
        assert "positive" in results
        assert "negative" in results
        assert "neutral" in results

if __name__ == '__main__':
    unittest.main()
