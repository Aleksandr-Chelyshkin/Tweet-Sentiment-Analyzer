
import tweepy
from textblob import TextBlob

def main():
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    # Authenticate with the Tweepy API
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Search for tweets about any product
    tweets = tweepy.Cursor(
        api.search_tweets,
        q="#product",
        count=100,
    ).items()

    # Analyze the sentiment of each tweet
    positive_tweets = 0
    negative_tweets = 0
    neutral_tweets = 0
    for tweet in tweets:
        sentiment = TextBlob(tweet.text).sentiment.polarity
        if sentiment > 0:
            positive_tweets += 1
        elif sentiment < 0:
            negative_tweets += 1
        else:
            neutral_tweets += 1

    # Print the results
    print("Number of positive tweets:", positive_tweets)
    print("Number of negative tweets:", negative_tweets)
    print("Number of neutral tweets:", neutral_tweets)

if __name__ == "__main__":
    main()
