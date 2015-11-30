#Fast Fashion Market Research


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Twitter Credentials can be obtained here https://apps.twitter.com/ 
access_token = '476641614-36djFqQ7T8smGaFOrqEcf4uEqopbEjb1MSshu6Mk'
access_token_secret = 'OVfyO9WNyc8GVefyoXzvCuAISLhlCjHP4l8IA4b3gP1pj'
consumer_key = 'yoDyTetxaQgmrAFEeYeCP1RVd'
consumer_secret = '2cZwrIywRDqDROtLefzOzD31UwDzGqxyCCHvAkVGIwisy4If8H'


#A listener that prints tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Stream will obtain the following terms: 'forever21', 'oldnavy', 'zara'
    stream.filter(track=['forever21', 'oldnavy', 'zara'])
