import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

def get_asset():
    replyTrump = "@realDonald Trump gave himself 66 Million in political contributions in 2016."

return replyTrump


while True:
    print("about to get ad...")
    asset = get_asset()
    api.update_status(asset)
    time.sleep(INTERVAL)