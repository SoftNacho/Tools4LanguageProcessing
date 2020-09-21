#!/usr/bin/python3

import sys
import nltk
from collections import defaultdict
# Import d.py
from d import Vocabulary

# PART C (10 points)
#
# Complete the body of this class 
#   by implementing the unimplemented methods

class Conditional:

    # Define a constructor
    #
    # For every pair of words (one from e, one from f),
    #    store the value provided by initial_value
    # 
    # HINT: In addition to storing the name and both vocabs,
    #       you will need to store a dictionary of dictionaries
    def __init__(self, name, e_vocab, f_vocab, initial_value):
        self.name = name
        self.e_vocab = e_vocab
        self.f_vocab = f_vocab
        #self.initial_value = 0
        self.dict_of_dict = defaultdict(dict)

        #storing initial value for every pair of words in dictionary of dictionaries
        for e_word in Vocabulary.words(e_vocab):
            for f_word in Vocabulary.words(f_vocab):
                self.dict_of_dict[e_word][f_word] = initial_value
#        print(self.dict_of_dict)
        
    # Given an integer index for a word from e and a word from f,
    #    return the corresponding value
    def get(self, e_i, f_i):
        e_word = Vocabulary.get_word(self.e_vocab, e_i)
        f_word = Vocabulary.get_word(self.f_vocab, f_i)
        #looking for value corresponding to dict of dict val
        ret_val = self.dict_of_dict[e_word][f_word]

        return ret_val

    # Given an integer index for a word from e and a word from f,
    #    store the value provided
    def set(self, e_i, f_i, value):
        e_word = Vocabulary.get_word(self.e_vocab, e_i)
        f_word = Vocabulary.get_word(self.f_vocab, f_i)

        self.dict_of_dict[e_word][f_word] = value

    # Return a string representation of this object
    #
    # See c.expected_output and test_c.py for the format of the string
    def __str__(self):
       ret_string = ""
 
       for e in Vocabulary.words(self.e_vocab):
           for f in Vocabulary.words(self.f_vocab):
               ret_string = ret_string + self.name + "[" + e + " | " + f + "]" + " = " + str(self.dict_of_dict[e][f]) + '\n'
       return ret_string


def create_vocab(words):
    v = Vocabulary()
    for word in words:
        v.get_int(word)
    return v


if __name__ == '__main__':

    if (len(sys.argv) > 2):
        f1 = open(sys.argv[1])
        raw1 = f1.read()
        words_e=nltk.word_tokenize(raw1)

        f2 = open(sys.argv[2])
        raw2 = f2.read()
        words_f=nltk.word_tokenize(raw2)

    else:
        words_e = nltk.word_tokenize("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")
        
        words_f = nltk.word_tokenize("Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como están de razón y conciencia, deben comportarse fraternalmente los unos con los otros.")

        e_v = create_vocab(words_e)
        f_v = create_vocab(words_f)
        
        count = Conditional("count", e_v, f_v, 0)
        print(count)
        print()
