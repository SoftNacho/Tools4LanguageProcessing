#!/usr/bin/python3
from d import tokenize
import nltk
from sys import stdin
# PART A (15%)
#
# Yupik syllables must be of the form:
#
# * CV
# * CVC
# * CVV
# * CVVC
#
# Additionally, the first syllable of a word may be of the form:
#
# * V
# * VC
# * VV
# * VVC
#
# Where C represents a Yupik consonant and V represents a Yupik vowel.
# 
#
# In all cases, the only instances of VV that are allowed are:
#
# * ii
# * aa
# * uu
#
#
# Yupik words may contain apostrophe (to separate otherwise ambiguous grapheme sequences).
#
#
# You will need to import tokenize from d.py
#
#
# Implement the violates_spelling_rules function.
# The function should take a string representing a word,
#     tokenize it using your tokenize function,
#     and return True if the word violates Yupik spelling rules (contains a non-Yupik grapheme or violates syllable structure),
#     and return False otherwise.
#
# 
# When this file is executed, it should:
#     * accept text from standard input
#     * tokenize it into words
#     * check each word to see if it violates Yupik spelling rules (using your function)
#     * and output a list of all words that violate Yupik spelling rules (one word per line)
#
# In other words, this program will function as a basic Yupik spell checker.
#
#
# No sample expected output will be provided for this program, but sample-ocr.txt contains many misspelled words.


def violates_spelling_rules(nd_word):
    letterV = ["i", "a", "u", "e"]
    letterC = ["p", "t", "k", "kw", "q", "qw", 
               "v", "l", "z", "y", "r", "g", "w", "gh", "ghw", 
               "f", "ll", "s", "rr", "gg", "wh", "ghh", "ghhw", "h",
               "m", "n", "ng", "ngw",
               "mm", "nn", "ngng", "ngngw"]
    letterVV = ["ii", "aa", "uu"]


    print(nd_word)
    word = ""
    nd_start = 0
    nd_end = len(nd_word)

    while nd_start < nd_end:
        if nd_start + 1 < nd_end and nd_word[nd_start] == "i" and nd_word[nd_start+1] == "i":  
            word = word + "ii"
            nd_start += 2
        elif nd_start + 1 < nd_end and nd_word[nd_start] == "a" and nd_word[nd_start+1] == "a":
            word = word + "aa"
            nd_start += 2
        elif nd_start + 1 < nd_end and nd_word[nd_start] == "u" and nd_word[nd_start+1] == "u":
            word = word + "uu"
            nd_start += 2
        elif nd_start + 1 < nd_end and nd_word[nd_start] == "k" and nd_word[nd_start+1] == "w":
            word = word + "kw"
            nd_start += 2
        else:
            word = word + nd_word[nd_start]
            nd_start += len(nd_word[nd_start])

    start = 0
    end = len(word)

    check = True

    while start < end:
        #VVC
        #making sure it is the first syllable and possible second syllable does NOT start with vowel
        if start + 2 == end-1 and start == 0 and word[0:2] in letterVV and word[2] in letterC:
            check = False
            start += 3
        elif start + 3 < end and start == 0 and word[0:2] in letterVV and word[2] in letterC and word[3] in letterC:
            check = False
            start += 3
      
        #VV
        #making sure it is the first syllable
        elif start + 1 < end and start == 0 and word[0:2] in letterVV:
            check = False 
            start += 2
        #VC
        #making sure it is the first syllable and possible second syllable does NOT start with vowel
        elif start + 1 == end-1 and start == 0 and word[0] in letterV and word[1] in letterC:
            check = False
            start += 2
        elif start + 2 < end and start == 0 and word[0] in letterV and word[1] in letterC and word[2] in letterC:
            check = False
            start += 2

        #V
        #making sure it is the first syllable
        elif start < end and start == 0 and word[0] in letterV:
            check = False
            start += 1

        #CVVC
        #making sure next vowel does NOT start with vowel
        elif start + 3 == end-1 and word[start] in letterC and word[start+1:start+3] in letterVV and word[start+3] in letterC:
            check = False
            start += 4
        elif start + 4 < end and word[start] in letterC and word[start+1:start+3] in letterVV and word[start+3] in letterC and word[start+4] in letterC:
            check = False
            start += 4

        #CVV
        elif start + 2 < end and word[start] in letterC and word[start+1:start+3] in letterVV:
            check = False
            start += 3

        #CVC
        #making sure next vowel does NOT start with vowel
        elif start + 2 == end-1 and word[start] in letterC and word[start+1] in letterV and word[start+2] in letterC:
            check = False
            start += 3
        elif start + 3 < end and word[start] in letterC and word[start+1] in letterV and word[start+2] in letterC and word[start+3] in letterC:
            check = False
            start += 3

        #CV
        elif start + 1 < end and word[start] in letterC and word[start+1] in letterV:
            check = False
            start += 2

        else:
            check = True
            break


    return check

def main():
    for input_sent in stdin:
        words = nltk.word_tokenize(input_sent)
        words = [str.lower(word.strip('.').strip(':').strip(',')) for word in words]
        for word in words:
            print(word, end = ': ')
            tokens = tokenize(word, True)
            if tokens != []:
                checked = violates_spelling_rules(tokens)
                if checked == False:
                    print("no spelling errors.", end = ' ')
                elif checked == True:
                    print("word is misspelled.", end = ' ')
        print('\n', end = '')


if __name__ == "__main__":
    main()

else: 
    exit
