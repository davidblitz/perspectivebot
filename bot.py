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
        print(status.text)
        if "is it just me" in status.text or "Is it just me" in status.text:
            if "RT @" in status.text:
                print(status.text)
                print("\n unfortunately a retweet :(")
            else:
                print(status.text)
                print("\n")
                user_handle = "@{}".format(status.user.screen_name)
                print(user_handle)
                print("\n")
                tweet_id = status.id
                print(tweet_id)
                print("\n")
                original_tweet = "twitter.com/{screen_name}/status/{tweet_id}".format(
                    screen_name = status.user.screen_name, tweet_id = tweet_id)
                message = "{msg} {original_tweet}".format(msg = messages[randint(0, 2)], original_tweet=original_tweet)
                print(message)
                api.update_status(message, in_reply_to_status_id = tweet_id)
                time.sleep(300)
        else:

            print(status.text)
            print("\n Not relevant \n")

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['is it just me'])
