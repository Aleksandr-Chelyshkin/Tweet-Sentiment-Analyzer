#!/usr/bin/env python3
import os
import tweepy
from dotenv import load_dotenv
from textblob import TextBlob

def main():
    # Load the stored environment variables
    load_dotenv()

    # Get the values
    api_key = os.getenv("api_key")
    api_secret = os.getenv("api_secret")
    access_token = os.getenv("access_token")
    access_token_secret = os.getenv("access_token_secret")

    # Authenticate with the Tweepy API
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Search for tweets about any product
    tweets = tweepy.Cursor(
        api.search_tweets,
        q="product name",
        count=100,
    ).items()

    # Analyze the sentiment of each tweet
    positive_tweets = [tweet for tweet in tweets if TextBlob(tweet.text).sentiment.polarity > 0]
    negative_tweets = [tweet for tweet in tweets if TextBlob(tweet.text).sentiment.polarity < 0]
    neutral_tweets = [tweet for tweet in tweets if TextBlob(tweet.text).sentiment.polarity == 0]

    # Print the results
    print("Number of positive tweets:", len(positive_tweets))
    print("Number of negative tweets:", len(negative_tweets))
    print("Number of neutral tweets:", len(neutral_tweets))

if __name__ == "__main__":
    main()
