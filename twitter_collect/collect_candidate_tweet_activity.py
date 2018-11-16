#Nous cherchons a récuperer et collecter en continu
# les tweets qui concernent le candidat/membre de son équipe
from TwitterPredictor.twitter_collect.twitter_connection_setup import *

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


def get_retweets_of_candidate(candidate):
    connection = twitter_setup()
    #récupére les tweet de la timeline
    tweets = connection.user_timeline(candidate,count=10)
    for status in tweets:
        # recupere les tweets originaux et non pas les RT
        retweets = connection.retweets(status.id,count=20)
        for tweet in retweets:
            print(tweet.text)


if __name__ == '__main__':
    #get_retweets_of_candidate('@sncfisajoke')
    get_replies('@sncfisajoke')


