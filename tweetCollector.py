#original code from https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./

import tweepy
import csv

consumer_key    = "RKyjK5AWmIupN6DXedPEoRgID"
consumer_secret    = "Fvo61NtRUULxO95gnN9hhDT0dnyuDS4UH3LuAmekoSDYSCa7n6"
access_token    = "43080622-yNYIS2U8lIdF66lia4QRdKWxwr16e6R7f0X7ILvbz"
access_token_secret = "O8YwovrNzqTpPAu1RdNzs4UDPXEz4q99PODvzslXEB50M"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)


searchQuery = '#ooutroladodoparaiso'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1


tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))

with open('ooutroladodoparaiso2.csv', 'a') as csvFile:
    csvWriter = csv.writer(csvFile)
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
            	if (not tweet.retweeted) and ('RT @' not in tweet.text):
            	    print (tweet.created_at, tweet.text)
            	    csvWriter.writerow([tweet.created_at, tweet.text])
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to ooutroladodoparaiso.csv'".format(tweetCount, fName))
