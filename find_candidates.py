import string

import csv

with open('world_cities.csv', mode='r') as infile:
        reader = csv.reader(infile)
        my_dict = {rows[0]: {rows[1]} for rows in reader}


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
    print(candidates)
    return candidates

def find_locations(candidates):
    location_list = []
    for n in candidates:
        try:
            if type(my_dict[n]) == set:
                location_list.append(n)
        except:
            pass
    return location_list
