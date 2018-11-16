import numpy as np
import tweepy
import panda

from twitter_collect.twitter_connection_setup import twitter_setup


def collect():
    connexion = twitter_setup()
    tab_tweet=[]
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        #print(tweet.text)
        tab_tweet += [tweet.text]
    return(tab_tweet)


#information la plus importante : les RT. on recupere le nombre moyen de RT sur le tableau

def nb_moyen_RT(data):
    RT_totaux =0
    for i in range (0,len(data['RTs'])):
        RT_totaux +=data['RTs'][i]
    return (RT_totaux//len(data['RTs']))

def liste_tweets_importants(data,nb_moyen_RT):
    liste= data[data.RTs > nb_moyen_RT].index[0]

def print_data():
    data = []
    data [0][0],data [0][1],data [0][2],data [0][3]='','tweet_textual_content','len','RTs'
    for i in range (1,len(collect())+1):
        data [i][0],data [i][1],data [i][2],data [i][3]=i-1,collect()[i-1],len(collect()[i-1]),''
    print(data)




if __name__ == '__main__':
    print_data()

