from twitter_auth import TwitterSentimentAnalyzer

def main():
    analyzer = TwitterSentimentAnalyzer()
    results = analyzer.analyze("product name")

    # Print the results
    print("Number of positive tweets:", results["positive"])
    print("Number of negative tweets:", results["negative"])
    print("Number of neutral tweets:", results["neutral"])

if __name__ == "__main__":
    main()
