#!/usr/bin/python3

import sys
import nltk
#from d import sort_by_length

# PART C (10 points)
#
# Define the novel10 function such that it accepts a list of strings,
#    splits the list into a list containing the first 90% of the items,
#                     and a list containing the last  10% of the items.
#
# Return a list of the unique tokens (sorted lexicographically) that appeared in the latter list but not in the former
#
def novel10(words):
    separation = int(len(words) * 0.9)
    ninety = words[:separation]
    ten = words[separation:]
    unique_list = []
    duplicate_list = []
    for tokens in ten:
        if tokens in ninety or tokens in unique_list:
            duplicate_list.append(tokens)
        else:
            unique_list.append(tokens)

#    unique_list = sort_by_length(unique_list)
    unique_list = sorted(unique_list)
    return unique_list


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        words=nltk.word_tokenize(sys.argv[1])
    else:
        words = nltk.corpus.udhr.words("English-Latin1")

    for word in novel10(words):
        print(word)
