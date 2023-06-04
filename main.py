import tweepy
import keys
import tweetCollection
import random


def tweet():
    text = tweetCollection.tweets[random.randint(
        0, len(tweetCollection.tweets))]

    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.acces_token, keys.acces_token_secret)
    client.create_tweet(text=text)

    print("Succes")


if __name__ == "__main__":
    # api = api()
    tweet()
