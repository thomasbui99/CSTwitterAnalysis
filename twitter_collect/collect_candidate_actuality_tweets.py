#On veut collecter tous les retweets d'un tweet d'un candidat ou d'un membre de son equipe
# #ou tous les tweets reply d'un tweet d'un candidat:

from TwitterPredictor.twitter_collect.twitter_connection_setup import *
from TwitterPredictor.twitter_collect.twitter_collect_whole import get_candidate_queries

twitter_api = twitter_setup()

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    #return all tweets responding to a list of queries
    tweets = twitter_api.search(queries,language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)


if __name__ == '__main__':
    print(get_tweets_from_candidates_search_queries(get_candidate_queries(1,'\\Users\\thoma\\PycharmProjects\\CodingWeek1\\CandidateData\\'),twitter_api))
