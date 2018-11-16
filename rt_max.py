import tweepy
from twitter_collect.credentials import *
import numpy as np
import pandas as pd


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


def collect_2():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)


def collect_3():
    connexion = twitter_setup()
    tab_tweet=[]
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        #print(tweet.text)
        tab_tweet += [tweet.text]
    return(tab_tweet)


def collect_to_pandas_dataframe():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']   = np.array([tweet.retweet_count for tweet in tweets])

    rt_max = np.max(data['RTs'])
    rt = data[data.RTs == rt_max].index[0]
# Max RTs:
    print("Le tweet le plus retrweeté est : \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))
    return data





if __name__ == '__main__':
    print(collect_to_pandas_dataframe())


