import twitter

# Replace with your actual Twitter API credentials
consumer_key = 'cXDqbaFAmlLgMA48GhZZVMavz'
consumer_secret = 'pHa89l3CtFFL5M8nj0AVgvGWg1p2eiOBTvRQE5MExK9g6zaaNn'
access_token = '1747112324950061056-lRNNAB6NdUZWG191nOuhYrfSaLM7xh'
access_token_secret = '1q8sdG6BK77zOMCyYXh5Hoh3cEP5WmbPJ6gZqch2WXdfr'

api = twitter.Api(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret)

results = api.GetSearch(term='Corona Outbreak', count=100)
for tweet in results:
    print(tweet.text)