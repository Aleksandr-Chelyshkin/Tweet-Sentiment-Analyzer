#!/usr/bin/env python3
import tweepy
from textblob import TextBlob

def main():
    credentials = {
        "api_key": "API_KEY",
        "api_secret": "API_SECRET",
        "access_token": "ACCESS_TOKEN",
        "access_token_secret": "ACCESS_TOKEN_SECRET"
    }

    api_key = credentials["api_key"]
    api_secret = credentials["api_secret"]
    access_token = credentials["access_token"]
    access_token_secret = credentials["access_token_secret"]

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
