#!/usr/bin/python3

import sys
import nltk

# PART A (15 points)
#
# Define the most_frequent_casing function 
#   such that it accepts a list of strings (representing a tokenized text)
#
# For each token, determine the most frequent casing of that token in the text.
#
# For example, if "The" occurs 18 times, "the" occurs 37 times, and "THE" occurs 2 times,
#    then the most frequent casing of this token is "the".
#
# Alternatively, if "Trump" occurs 15 times, and "trump" appears 1 time, 
#    then the most frequent casing of this token is "Trump".
#
# If two or more variant casings are tied for the most occurrances,
#    select the one that occured first in the text.
#
# This function should return a dictionary whose keys are lowercase tokens
#    and whose values are the corresponding most frequent casing of that token.
#
def most_frequent_casing(tokenized_text):
    dictionary = {}
 
    for token in tokenized_text:
        all_caps_count = 0
        all_lower_count = 0
        majuscule_count = 0

        for tokens in tokenized_text:
            if token.lower() == tokens.lower():
                if tokens == tokens.upper():
                    all_caps_count += 1

                elif tokens == tokens.lower():  
                    all_lower_count += 1

                elif tokens[0] == tokens[0].upper() and tokens[1:] == tokens[1:].lower():
                    majuscule_count += 1

        #if word more frequent in all caps
        if all_caps_count > all_lower_count and all_caps_count > majuscule_count:
            dictionary[token.lower()] = token

        #if word more frequent in all lower case
        elif all_lower_count > all_caps_count and all_lower_count > majuscule_count:
            dictionary[token.lower()] = token

        #if work more frequent capitalized
        elif majuscule_count > all_caps_count and majuscule_count > all_lower_count: 
            dictionary[token.lower()] = token

        #if anything equal, take first case
        elif all_caps_count == all_lower_count or all_lower_count == majuscule_count or majuscule_count == all_caps_count:
            for token2 in tokenized_text:
                if token2.lower() == token.lower():
                    dictionary[token.lower()] = token2
                    break

    return dictionary

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        f = open(sys.argv[1])
        raw = f.read()
        words=nltk.word_tokenize(raw)
    else:
        words = nltk.word_tokenize('The man walked across the street and into the building. "Into the Wild" was one of his favorite movies.')

    d = most_frequent_casing(words)

    for word in words:
        print(d[word.lower()])
