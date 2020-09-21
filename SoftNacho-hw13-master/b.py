#!/usr/bin/python3

import sys
import nltk
import math

from d import Vocabulary
from c import Conditional

# PART B (10 points)
#
# Complete the body of this class 
#   by implementing the unimplemented methods.
#
# See instructions/b.pdf for details


class ParallelCorpus:

    # Define a constructor
    def __init__(self):

        # List of English sentences. Each sentence will be represented as a list of ints.
        self.e = list() 

        # List of foreign sentences  Each sentence will be represented as a list of ints.
        self.f = list() 

        # Initially empty vocabularies
        self.e_vocab = Vocabulary()
        self.f_vocab = Vocabulary()


    # Returns the number of sentence pairs that have been added to this parallel corpus
    def size(self):
        return len(self.e)

    # Returns the list of integers corresponding to the English sentence at the specified sentence index
    def get_e(self, sentence_index):
        return self.e[sentence_index]

    # Returns the list of integers corresponding to the foreign sentence at the specified sentence index
    def get_f(self, sentence_index):
        return self.f[sentence_index]


    # Given a string representing an English sentence
    #   and a string representing a foreign sentence,
    #   tokenize each string using nltk.word_tokenize,
    #   and use the appropriate vocabulary to convert each token to an int.
    #   
    # Append the list of integers (corresponding to the English sentence) to self.e
    # Append the list of integers (corresponding to the foreign sentence) to self.f
    def add(self, e, f):
        #tokenizing the sentences
        english_words = nltk.word_tokenize(e)
        foreign_words = nltk.word_tokenize(f)

        #creating lists to store variables
        english_list = list()
        foreign_list = list()

        #going through each word of sentence to find the corresponding int and append to list
        for english_word in english_words:
            cur_int = Vocabulary.get_int(self.e_vocab, english_word)
            english_list.append(cur_int)

        for foreign_word in foreign_words:
            cur_int = Vocabulary.get_int(self.f_vocab, foreign_word)
            foreign_list.append(cur_int)

        #appending list to of int to self.? 
        self.e.append(english_list)
        self.f.append(foreign_list)


    # Construct a conditional distribution with the given name.
    #
    # Use the formula given in the supplementary instructions
    def create_uniform_distribution(self, name):
        #use constructor of Conditional class
        init_val = 1 / self.f_vocab.size()
#        print(init_val)
        return Conditional(name, self.e_vocab, self.f_vocab, init_val) 

    # Given a sentence index, a scaling factor epsilon, and a conditional distribution,
    #    calculate the conditional probability 
    #    of the English sentence (at that sentence index) 
    #    given the foreign sentence (at that sentence index)
    #
    # Use the formula given in the supplementary instructions
    def conditional_probability(self, sentence_index, epsilon, conditional):
        #getting int from sentences at sentence_index
        english = self.get_e(sentence_index)
        foreign = self.get_f(sentence_index)
#        print(english)
#        print(foreign)

        #using formula from PDF to initialize operands of prob
        factor = epsilon / (len(english) * len(foreign))
        sum_of_sum = 0
#        print(factor)    
 
        #gathering values of each word 
        for j in range(0, len(english)):
            for i in range(0, len(foreign)):
                new_val = conditional.get(english[j], foreign[i])
#                print(new_val)
                sum_of_sum = sum_of_sum + new_val
#                print(sum_of_sum)

        cond_prob = factor * sum_of_sum
        return cond_prob    


    # Given a conditional distribution and a scaling factor epsilon,
    #    calculate the perplexity of this parallel corpus.
    #
    # Use the formula given in the supplementary instructions
    def perplexity(self, epsilon, conditional):
        sum_perx = 0
        range_bound = self.size()
#        print(range_bound)
        #following formula from PDF
        for s in range(0, range_bound):
#            print(s)
            temp = self.conditional_probability(s, epsilon, conditional)
#            print(temp)
            new_val_2 = math.log2(temp)
            sum_perx = sum_perx + new_val_2

        PP = -1 * sum_perx
        return PP



if __name__ == '__main__':
    
    corpus = ParallelCorpus()

    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        for line in f:
            e,f = line.split("\t")
            corpus.add(e,f)

    else:

        corpus.add("the house", "das Haus")
        corpus.add("the book",  "das Buch")
        corpus.add("a book",    "ein Buch")

        
    epsilon = 0.01
    t = corpus.create_uniform_distribution("t")
    ppl = corpus.perplexity(epsilon, t)
    print(t)
    print()
    print(ppl)
