import argparse
import unittest
from Tweets_Analyzer import TwitterSentimentAnalyzer as BaseTwitterSentimentAnalyzer
import tweepy

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Analyze Twitter sentiments")

# Add arguments for the API keys and tokens
parser.add_argument("--api_key", required=True, help="Twitter API key")
parser.add_argument("--api_secret", required=True, help="Twitter API secret key")
parser.add_argument("--access_token", required=True, help="Twitter access token")
parser.add_argument("--access_token_secret", required=True, help="Twitter access token secret")

# Parse the command-line arguments
args = parser.parse_args()

# Get the values from the arguments
api_key = args.api_key
api_secret = args.api_secret
access_token = args.access_token
access_token_secret = args.access_token_secret

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
