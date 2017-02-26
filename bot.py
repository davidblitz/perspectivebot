import time
from random import randint
import tweepy

CONSUMER_KEY = 'YOUR CONSUMER KEY HERE'
CONSUMER_SECRET = 'YOUR CONSUMER_SECRET HERE'
ACCESS_KEY = 'YOUR ACCESS_KEY HERE'
ACCESS_SECRET = 'YOUR ACCESS_SECRET HERE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

messages = ["I'm afraid it's just you.", "I'm perspectiveBot and it's just you. :*", "I asked my friends - it's just you."]
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        user_handle = "@{}".format(status.user.screen_name)
        tweet_id = status.id
        message = "{handle} {msg}".format(handle = user_handle, msg = messages[randint(0, 2)])
        api.update_status(message, tweet_id)
        time.sleep(300)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['is it just me'])

