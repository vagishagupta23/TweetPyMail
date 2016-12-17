from __future__ import absolute_import, print_function
import forecastio
import json
import tweepy
#import key
import requests
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
def func2():
        ckey='5S6e3TQH89WniAr1rnHKkZPNp'
        csecret='WD9GN0uzOqjsMfYwLfum1d921dagIpXmGmc62VqvHfHQVs63NC'
        atoken='2972097164-93xYPs0F3ilWa6f9ogAywqX0kcO9dCyNF6A3ZU4'
        asecret='WGQw1sE74oarrfRs5HUo2IAdb8FUlUzAawgxE9JnoLcye'
        auth=OAuthHandler(ckey,csecret)
        auth.set_access_token(atoken,asecret)
        #twitterStream=Stream(auth,listener())
        api=tweepy.API(auth)
        res = requests.get("https://contesttrackerapi.herokuapp.com/")
        #convert to py dict
        res = json.loads(res.text)
        upcoming = res["result"]["upcoming"]
        tweet = "Next contest: " + upcoming[0]["StartTime"] + "on " + upcoming[0]["Platform"] +". "+ upcoming[0]["url"]
        #api.update_status(status='[TWEETMAIL]' + tweet)
        rls=[res["result"]["upcoming"][i] for i in xrange(9,len(res["result"]["upcoming"]))]
        tweet=rls[0]
        print(rls[0])
        tw="UPCOMING CHALLENGE: "+rls[0]["Name"]+" on "+rls[0]["Platform"]+" from "+rls[0]["StartTime"]+" for "+rls[0]["Duration"]+" till "+rls[0]["EndTime"]
        print(tw)
        api.update_status(status='[TWEETMAIL]' + tw)

def main():
        func2()
if __name__ == "__main__": main()
