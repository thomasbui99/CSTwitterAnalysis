#Anlysons plus en profondeur

import numpy as np
import pandas as pd
from TwitterPredictor.twitter_collect.twitter_connection_setup import twitter_setup


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
    return data

def print_rt_max():
    data = collect_to_pandas_dataframe()
    #Tweet avec le plus de retweets
    rt_max = np.max(data['RTs'])
    rt = data[data.RTs == rt_max].index[0]
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

def print_likes_max():
    data = collect_to_pandas_dataframe()
    #Tweet avec le plus de likes
    likes_max = np.max(data['Likes'])
    likes = data[data.Likes == likes_max].index[0]
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][likes]))
    print("Number of likes: {}".format(likes_max))

def print_reply_max():
    data = collect_to_pandas_dataframe()
    #Tweet avec le plus de reponses
    reply_max = np.max(data['Replies'])
    reply = data[data.Replies == reply_max].index[0]
    print("The tweet with more replies is: \n{}".format(data['tweet_textual_content'][reply]))
    print("Number of replies: {}".format(reply_max))


if __name__ == '__main__':
    print(collect_to_pandas_dataframe())
