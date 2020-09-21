#!/usr/bin/python3
from sys import stdin
import nltk
# PART D (65%)
#
# Define a function called tokenize that accepts a lowercased Yupik word,
# and tokenizes it into Yupik graphemes.
#
# Punctuation within words (apostrophes, etc) is used to separate distinct graphemes
# when they would otherwise be confusable.
#
# For example, "n" followed by "g" would be indicated "n'g" to prevent confusion with "ng"
#
# If the word contains such an apostrophe, then you should use the keep_apostrophes parameter.
# If this parameter is set to True, then you should include the apostrophe in the list of graphemes.
# Otherwise, you should not include the apostrophe in the list of graphemes
#
# Sometimes, your function may be passed an English loan word.
# Such a word is likely to contain alphabetic characters that are not in the Yupik alphabet.
# If a word contains any alphabetic characters that are not in the Yupik alphabet,
#    any such character should be tokenized as an individual token.
#
# For example, the sample text contains the word culturemeng
# 
# The result of tokenize("culturemeng") 
#     should be the list ['c', 'u', 'l', 't', 'u', 'r', 'e', 'm', 'e', 'ng']
#
# If the word contains a character that is not alphabetic and is not an apostrophe,
#     you should discard it.
#
# Sometimes, a word could be tokenized multiple ways, but only one of them will be correct.
# You should implement a greedy longest match, starting at the end of the word.
#
# For example:
#
# The result of tokenize("aanghuutuq")
#     should be the list ['a', 'a', 'n', 'gh', 'u', 'u', 't', 'u', 'q']
#
# The result of tokenize("neghneghngwaaq")
#     should be the list ['n', 'e', 'gh', 'n', 'e', 'gh', 'ngw', 'a', 'a', 'q']
#
#
# When this program is run, it should accept text from standard input,
# lowercase it, remove punctuation outside words, and use your function
# to tokenize it into Yupik graphemes (with keep_apostrophes=False).
#
# Punctuation outside words should be disregarded.


def tokenize(word, keep_apostrophes):
    reversed_word = word[::-1]
    apostrophe = '\''
    ret = []
    ret_final = []

    while len(reversed_word) > 0:    
        #if "ngngw" recognized
        if len(reversed_word) >= 5 and reversed_word[0] == 'w' and reversed_word[1] == 'g' and reversed_word[2] == 'n' and reversed_word[3] == 'g' and reversed_word[4] == 'n':
            ret = ['ngngw'] + ret
            reversed_word = reversed_word[5:]

        #if "ngng" recognized
        elif len(reversed_word) >= 4 and reversed_word[0] == 'g' and reversed_word[1] == 'n' and reversed_word[2] == 'g' and reversed_word[3] == 'n':
            ret = ['ngng'] + ret
            reversed_word = reversed_word[4:]

        #if "ghhw" recognized
        elif len(reversed_word) >= 4 and reversed_word[0] == 'w' and reversed_word[1] == 'h' and reversed_word[2] == 'h' and reversed_word[3] == 'g':
            ret = ['ghhw'] + ret
            reversed_word = reversed_word[4:]

        #if "ngw" recognized
        elif len(reversed_word) >= 3 and reversed_word[0] == 'w' and reversed_word[1] == 'g' and reversed_word[2] == 'n':
            ret = ['ngw'] + ret
            reversed_word = reversed_word[3:]

        #if "ghw" recognized
        elif len(reversed_word) >= 3 and reversed_word[0] == 'w' and reversed_word[1] == 'h' and reversed_word[2] == 'g':
            ret = ['ghw'] + ret
            reversed_word = reversed_word[3:]

        #if "ghh" recognize
        elif len(reversed_word) >= 3 and reversed_word[0] == 'h' and reversed_word[1] == 'h' and reversed_word[2] == 'g':
            ret = ['ghh'] + ret
            reversed_word = reversed_word[3:]

        #if "kw" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'w' and reversed_word[1] == 'k':
            ret = ['kw'] + ret
            reversed_word = reversed_word[2:]

        #if "qw" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'w' and reversed_word[1] == 'q':
            ret = ['qw'] + ret
            reversed_word = reversed_word[2:]

        #if "gh" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'h' and reversed_word[1] == 'g':
            ret = ['gh'] + ret
            reversed_word = reversed_word[2:]

        #if "ll" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'l' and reversed_word[1] == 'l':
            ret = ['ll'] + ret
            reversed_word = reversed_word[2:]

        #if "rr" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'r' and reversed_word[1] == 'r':
            ret = ['rr'] + ret
            reversed_word = reversed_word[2:]

        #if "gg" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'g' and reversed_word[1] == 'g':
            ret = ['gg'] + ret
            reversed_word = reversed_word[2:]

        #if "wh" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'h' and reversed_word[1] == 'w':
            ret = ['wh'] + ret
            reversed_word = reversed_word[2:]
            
        #if "ng" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'g' and reversed_word[1] == 'n':
            ret = ['ng'] + ret
            reversed_word = reversed_word[2:]

        #if "mm" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'm' and reversed_word[1] == 'm':
            ret = ['mm'] + ret
            reversed_word = reversed_word[2:]
            
        #if "nn" recognize
        elif len(reversed_word) >= 2 and reversed_word[0] == 'n' and reversed_word[1] == 'n':
            ret = ['nn'] + ret
            reversed_word = reversed_word[2:]

        elif len(reversed_word) >= 1:
            ret = [reversed_word[0]] + ret
            reversed_word = reversed_word[1:]
        
    if keep_apostrophes == False:
        for token in ret:
            if token != '\'':
                ret_final = ret_final + [token] 
    else:
        ret_final = ret
     
    return ret_final



def main():
    for input_sent in stdin:
        words = nltk.word_tokenize(input_sent)
        words = [str.lower(word.strip('.').strip(':').strip(',')) for word in words]
        words = [tokenize(word, False) for word in words] 

        for word in words:
            if len(word) > 0:
                print(word, end = ' ')
        print('\n', end = '')



if __name__ == "__main__":
    main()

else: 
    exit
