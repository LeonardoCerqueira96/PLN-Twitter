import tweepy
import numpy as py

def main():
    my_consumer_key    = "RKyjK5AWmIupN6DXedPEoRgID"
    my_consumer_sec    = "Fvo61NtRUULxO95gnN9hhDT0dnyuDS4UH3LuAmekoSDYSCa7n6"
    my_access_token    = "43080622-yNYIS2U8lIdF66lia4QRdKWxwr16e6R7f0X7ILvbz"
    my_access_secret   = "O8YwovrNzqTpPAu1RdNzs4UDPXEz4q99PODvzslXEB50M"

    output_file = open("out.txt", "w+", encoding='utf-8')

    auth = tweepy.OAuthHandler(my_consumer_key, my_consumer_sec)
    auth.set_access_token(my_access_token, my_access_secret)

    api = tweepy.API(auth)

    query = 'ooutroladodoparaiso'
    max_tweets = 1000
    language = 'pt'
    results = api.search(q="ooutroladodoparaiso", lang="pt", count=20)

    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, , lang=language, count=count, since_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            break

    for tweet in results:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            output_file.write(tweet.text)
            output_file.write("\n\n")

    output_file.close()

if __name__ == "__main__":
    main()

