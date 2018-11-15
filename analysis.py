import numpy as np
import tweepy
import panda

from twitter_collect.twitter_connection_setup import twitter_setup


def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)


#information la plus importante : les RT. on recupere le nombre moyen de RT sur le tableau

def nb_moyen_RT(data):
    RT_totaux =0
    for i in range (0,len(data['RTs'])):
        RT_totaux +=data['RTs'][i]
    return (RT_totaux//len(data['RTs']))

def liste_tweets_importants(data,nb_moyen_RT):
    liste= data[data.RTs > nb_moyen_RT].index[0]


