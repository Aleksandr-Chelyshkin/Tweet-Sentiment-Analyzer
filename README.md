# twitter-API
This python code analyzes the sentiment of tweets about any topic.

It first imports the tweepy and textblob modules. Then, it defines two variables for the Twitter API key and secret. Next, it uses the tweepy module to authenticate with the Twitter API and search for tweets about the specified topic. The search returns a list of tweets, which the script iterates over. For each tweet, the script uses the textblob module to calculate the sentiment of the tweet and prints it to the console.

For the code to work properly it's crucial to log in to your Twitter developer account and go to the Apps management screen. From there, click on the Details for your app and then click on the Keys and tokens tab. You should be able to see your API key and secret key there as well as tokens. 
