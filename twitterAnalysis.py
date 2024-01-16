import twitter

# Replace with your actual Twitter API credentials
consumer_key = 'your api key'
consumer_secret = 'your api key secret'
access_token = 'your access token'
access_token_secret = 'your access token secret'

api = twitter.Api(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret)

results = api.GetSearch(term='Corona Outbreak', count=100)
for tweet in results:
    print(tweet.text)
