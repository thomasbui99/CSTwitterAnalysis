def get_candidate_queries(num_candidate, path_file, type):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """

    keywords_num_candidate = ""
    hashtags_num_candidate = ""

    if type == "keywords":
        with open (path_file, "r") as keywords:
            if num_candidate == 1:
                keywords_num_candidate = keywords.readline() # readline() gives you 1 line
                return keywords_num_candidate
            else:
                for ligne in range(1,3):
                    keywords_num_candidate = keywords.readline()
                return  keywords_num_candidate
    else:
        with open (path_file, "r") as hashtags:
            if num_candidate == 1:
                hashtags_num_candidate = hashtags.readline() # readline() gives you 1 line
                return hashtags_num_candidate
            else:
                for ligne in range(1,3):
                    hashtags_num_candidate = hashtags.readline()
                return  hashtags_num_candidate



if __name__ == '__main__':
    print(get_candidate_queries(num_candidate=2, path_file='C:\\Users\\thoma\\PycharmProjects\\TwitterPredictor\\CandidateData\\keywords_candidate_num_candidate.txt', type="keywords"))






