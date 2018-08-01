import string

import csv

with open('world_cities.csv', mode='r') as infile:
        reader = csv.reader(infile)
        my_dict = {rows[0]: {rows[1]} for rows in reader}


article_link = input("Enter the url of the article")
def find_candidates(story):

    transtable = str.maketrans({key: " " for key in string.punctuation})
    article_text = str(story)
    article_text_stripped = article_text.translate(transtable)
    article_list = article_text_stripped.split()
    candidates = []


    for word in article_list:
        for c in string.ascii_uppercase:
            if c in word:
                candidates.append(word)
    return candidates

for n in find_candidates(article_link):
    try:
        if type(my_dict[n]) == set:
            print(n, my_dict[n])
    except:
        pass
