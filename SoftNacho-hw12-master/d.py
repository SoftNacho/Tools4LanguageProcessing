#!/usr/bin/python3

import sys
import nltk

# PART D (65 points)
#
# Define the sort_by_length function such that it accepts a list of strings
#   and returns that list such that the items are sorted by length.
#
# If there are multiple strings of the same length, they should be sorted lexicographically.
#     (see https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types)
#
# For example: in lexicographic sorting, "A" < "a", and "Zoo" < "box"
#
# You are encouraged to use the code at http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# as a starting point for implementing your sort_by_length function

def sort_by_length(words):
    sorted_list = []
    
    if len(words)>1:
        mid = len(words)//2
        lefthalf = words[:mid]
        righthalf = words[mid:]

        lefthalf = sort_by_length(lefthalf)
        righthalf = sort_by_length(righthalf)

        i=0
        j=0 
        k=0
        

        while i < len(lefthalf) and j < len(righthalf):
            #sorting by length
            if len(lefthalf[i]) < len(righthalf[j]):
                sorted_list.append(lefthalf[i])
                i=i+1

            elif len(lefthalf[i]) > len(righthalf[j]):
                sorted_list.append(righthalf[j])
                j=j+1

            #sorting lexicographically      
            else:
                if lefthalf[i] < righthalf[j]:
                    sorted_list.append(lefthalf[i])
                    i += 1
                else:
                    sorted_list.append(righthalf[j])
                    j += 1
            k=k+1

        while i < len(lefthalf):
            sorted_list.append(lefthalf[i])
            i=i+1
            k=k+1

        while j < len(righthalf):
            sorted_list.append(righthalf[j])
            j=j+1
            k=k+1

        return sorted_list

    else:
        return words


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        f = open(sys.argv[1])
        raw = f.read()
        words=nltk.word_tokenize(raw)
    else:
        words = nltk.word_tokenize("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")

    for word in sort_by_length(words):
        print(word)
