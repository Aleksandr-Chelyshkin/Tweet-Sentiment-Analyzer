import os
import tweepy
from collections import Counter
from dotenv import load_dotenv
from textblob import TextBlob

# Load the stored environment variables
load_dotenv()

# Get the values
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

class TwitterSentimentAnalyzer:
    def __init__(self):
        # Authenticate with the Tweepy API
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def analyze(self, query):
        # Search for tweets about any product
        tweets = tweepy.Cursor(
            self.api.search_tweets,
            q=query,
            count=100,
        ).items()

        # Count the number of positive, negative, and neutral tweets
        sentiment_counts = Counter(TextBlob(tweet.text).sentiment.polarity for tweet in tweets)
        positive_count = sentiment_counts[1]
        negative_count = sentiment_counts[-1]
        neutral_count = sentiment_counts[0]

        # Return the results
        return {
            "positive": positive_count,
            "negative": negative_count,
            "neutral": neutral_count
        }

