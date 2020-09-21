#!/usr/bin/python3

import sys
import nltk

# PART B (10 points)
#
# Define the sorted_brown_tags function such that
#   it returns a sorted list of the tags used in the Brown corpus, removing duplicates.
#
def sorted_brown_tags():
    tag_list = []

    #tag has pattern (word, tag) but only need tag
    for (word, tag) in nltk.corpus.brown.tagged_words(tagset='brown'):
        if tag not in tag_list:
            tag_list.append(tag)

    tag_list = sorted(tag_list)

    return tag_list

if __name__ == "__main__":
    for tag in sorted_brown_tags():
        print(tag)
