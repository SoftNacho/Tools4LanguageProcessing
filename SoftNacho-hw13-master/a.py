#!/usr/bin/python3

import sys
import nltk

from d import Vocabulary
from c import Conditional
from b import ParallelCorpus

# PART A (15 points)
#
# Complete the body of this class 
#   by implementing the unimplemented methods.
#
# See instructions/a.pdf for details

class IBM_Model1:

    def __init__(self, parallel_corpus):
        self.parallel_corpus = parallel_corpus
        self.t = parallel_corpus.create_uniform_distribution("t")

    def compute_normalization(self, e_sentence, f_sentence):
        #creating dictionary 'z'
        z = dict()
        z_e = 0

        for e in e_sentence:
            for f in f_sentence:
                z_e = z_e + self.t.get(e, f)

            z[e] = z_e
            #resetting z_e to 0 not to interfere with next normalization factor
            z_e = 0

        return z



    def update_counts(self, e_sentence, f_sentence, counts, z):
        for e in e_sentence:
            for f in f_sentence:
#                counts = counts + self.t.get(e, f) / z[e]
                #use formula from PDF
                counts.set(e, f, counts.get(e, f) + (self.t.get(e, f) / z[e])) 

    def update_totals(self, e_sentence, f_sentence, totals, z):
        for e in e_sentence:
            for f in f_sentence:
                #use formula from PDF
                totals[f] = totals[f] + self.t.get(e, f) / z[e]

    def update_probabilities(self, counts, totals):
        range_bound = self.parallel_corpus.size()
        
        #creating lists to use as index to set new probabilities
        english_list = list()
        foreign_list = list()

        #creating temporary arrays to get individual values of words
        eng = []
        frg = []

        for i in range (0, range_bound):
            eng = self.parallel_corpus.get_e(i)
            frg = self.parallel_corpus.get_f(i)
       
            for e in eng:
                english_list.append(e)

            for f in frg:
                foreign_list.append(f)


#        print(english_list)
#        print(foreign_list)

        for e in english_list:
            for f in foreign_list:
                self.t.set(e, f, counts.get(e, f) / totals[f])


    def initialize_totals(self):
        range_bound = self.parallel_corpus.size()

        totals = dict()
        #need to add foreign words list
        foreign_list = list()

        #same as previous function, create temp array

        for i in range(0, range_bound):
            frg = self.parallel_corpus.get_f(i)

            for f in frg:
                foreign_list.append(f)

        for f in foreign_list:
            totals[f] = 0.0

        return totals


    def process_sentence_pair(self, sentence_index, counts, totals):
        e_sentence = self.parallel_corpus.get_e(sentence_index)
        f_sentence = self.parallel_corpus.get_f(sentence_index)
        
        z = self.compute_normalization(e_sentence, f_sentence)
        
        self.update_counts(e_sentence, f_sentence, counts, z)
        self.update_totals(e_sentence, f_sentence, totals, z)


    def expectation_maximization(self):
        counts = Conditional("count", 
                             self.parallel_corpus.e_vocab, 
                             self.parallel_corpus.f_vocab, 
                             0.0)

        totals = self.initialize_totals()

        for sentence_index in range(0, self.parallel_corpus.size()):
            self.process_sentence_pair(sentence_index, counts, totals)

        self.update_probabilities(counts, totals)



    def estimate_model(self, epsilon, delta, max_iterations=100, verbose=0):

        iterations = 0
        old_ppl = float("inf")
        new_ppl = self.parallel_corpus.perplexity(epsilon, self.t)

        while (old_ppl - new_ppl > delta and iterations < max_iterations):

            if verbose >= 1:
                print("Iteration {}: perplexity {} --> {}".format(iterations, old_ppl, new_ppl))
            if verbose >= 3 or (verbose >= 2 and iterations==0):
                print(self.t)

            self.expectation_maximization()

            old_ppl = new_ppl
            new_ppl = self.parallel_corpus.perplexity(epsilon, self.t)

            iterations += 1

        if verbose >= 1:
            print("Iteration {}: perplexity {} --> {}".format(iterations, old_ppl, new_ppl))
        if verbose >= 2:
            print(self.t)



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

    model1 = IBM_Model1(corpus)
    epsilon = 0.01
    delta = 0.1

    model1.estimate_model(epsilon, delta, max_iterations=50, verbose=3)

    ppl = model1.parallel_corpus.perplexity(epsilon, model1.t)
    print()
    print(ppl)
