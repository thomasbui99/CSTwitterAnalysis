# Ici nous allons collecter les tweets où figurent noms des candidats, nom des partis, hashtags associees
# A l'aide des keywords, nous allons filter les tweets

def get_candidate_queries(num_candidate, file_path):

    """Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
:   return: (list) a list of string queries that can be done to the search API independently"""

    try:
        fichier = open(file_path + 'keywords_candidate_' + str(num_candidate) + '.txt','r')
        texte = fichier.read()
        liste = texte.splitlines()
        res = ""
        for keywords in liste:
            if res == "":
                res += keywords
            else:
                res += " OR " + keywords
        fichier = open(file_path + 'hashtags_candidate_' + str(num_candidate) + '.txt','r')
        texte = fichier.read()
        liste = texte.splitlines()
        for hashtags in liste:
            if res == "":
                res += hashtags
            else:
                res += " OR " + "#" + hashtags
        return res
    except IOError:
        print("404 Not found")


if __name__ == '__main__':
    print(get_candidate_queries(1,'C:\\Users\\thoma\\PycharmProjects\\CodingWeek1\\CandidateData\\'))

