
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
OAUTH_TOKEN = config.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = config.OAUTH_TOKEN_SECRET
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

mathcs_twitter_api = twitter.Twitter(auth=auth)
