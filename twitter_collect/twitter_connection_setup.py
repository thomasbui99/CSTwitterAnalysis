#  ECRIRE les fonctions nécessaires
# pour une connexion à l'API Twitter.

import tweepy
# We import our access keys:
from TweeterPredictor.credentials import *
from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


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

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel AND Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['@TheoMcrey'])

def get_replies(user_id):
   connexion = twitter_setup()
   replies=[]
    #recupere les messages recents du candidat  user_id
   for full_tweet in connexion.user_timeline(id = user_id,language="fr",rpp=100):
       print(full_tweet.text)
       #query pour retrouver des tweets repondant a l'utilisateur used_id
       query = 'to:'+user_id
       print(query)

       for tweet in connexion.search(q=query, since_id=992433028155654144, result_type='recent',timeout=999999):
           print(tweet.text)
            #si le tweet renvoye par la requete possede un champs "in reply_to__status_id_str" cest a dire si cest une reponse a un tweet
           if hasattr(tweet, 'in_reply_to_status_id_str'):
                # si c'ets une reponse au tweet actuel (full_tweet) du candidat
               if (tweet.in_reply_to_status_id_str==full_tweet.id_str):
                   replies.append(tweet.text)
                   print(tweet.text)

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        # TO COMPLETE
    except IOError:
        # TO COMPLETE
    return 0


def get_tweets_from_candidates_search_queries(queries, twitter_api):
    return 0




if __name__ == '__main__':
    #print(twitter_setup())
    #collect()
    #print(collect_by_user("@TheoMcrey"))
    #print(collect_by_streaming())
    print(get_replies("@TheoTZ"))
    print(get_candidate_queries("@TheoTZ"))
