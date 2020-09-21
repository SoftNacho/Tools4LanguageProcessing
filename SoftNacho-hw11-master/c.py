#!/usr/bin/python3
from sys import stdin
import nltk
from d import tokenize
# PART C (10%)
#
# Yupik has voiced and voiceless nasals and fricatives.
#
# Certain Yupik fricatives and nasals are "doubleable";
#    that is, they exist in voiced/voiceless pairs
#    where the voiced/voiceless distinction is denoted graphemically through "doubling":
#
# l   -> ll
# r   -> rr
# g   -> gg
# gh  -> ghh
# ghw -> ghhw
# n   -> nn
# m   -> mm
# ng  -> ngng
# ngw -> ngngw
#
#
# The remaining Yupik consonants do not show this doubling pattern.
#
# For each tokenized word, apply the following automatic devoicing rules:
#
# 1a) If an undoubled (but doubleable) fricative occurs immediately before OR after an unvoiced consonant
#     (where that other consonant is not doubleable),
#     the grapheme for the doubleable voiced fricative is replaced with its voiceless counterpart.
#
# 2) If an undoubled (but doubleable) nasal occurs immediately after an unvoiced consonant
#     (where that other consonant is not doubleable), 
#     the grapheme for the doubleable voiced nasal is replaced with its voiceless counterpart.
#
# 3a) If an undoubled (but doubleable) nasal or fricative occurs immediately after an unvoiced fricative
#     (where that other consonant is doubled),
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
#
# 3b) If an undoubled (but doubleable) nasal or fricative occurs immediately before the unvoiced fricative ll
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
#
# Implement a function called apply_devoicing that accepts a list of graphemes,
#     and returns a list of graphemes with the above rules applied.
#
# When this file is executed, it should:
#    * accept text from standard input,
#    * lowercase it,
#    * tokenizes it into Yupik graphemes using the tokenize function from d.py (with keep_apostrophes=True), 
#    * apply the devoicing rules by calling your apply_devoicing function, 
#    * and print the corresponding output (formatted as words, not lists of graphemes).
#
# (Note: you must import tokenize from d.py)



def apply_devoicing(graphemes):
    ret = ''
    doubleable_fricative = ['l', 'r', 'g', 'gh', 'ghw']
    doubleable_nasal = ['n', 'm', 'ng', 'ngw']
    unvoiced_consonants_nd = ['f', 's', 'wh', 'h', 'p', 't', 'k', 'kw', 'q', 'qw']
    unvoiced_fricative_doubled = ['ll', 'rr', 'gg', 'ghh', 'ghhw']
     
    #Rule 1a)
    for i in range(0, len(graphemes)):
        if graphemes[i] in doubleable_fricative:
            if (i < len(graphemes) and graphemes[i+1] in unvoiced_consonants_nd) or (i > 0 and graphemes[i-1] in unvoiced_consonants_nd):
                if graphemes[i] == 'l':
                    graphemes[i] = 'll'

                elif graphemes[i] == 'r':
                    graphemes[i] = 'rr'
     
                elif graphemes[i] == 'g':
                    graphemes[i] = 'gg'

                elif graphemes[i] == 'gh':
                    graphemes[i] = 'ghh'
 
                elif graphemes[i] == 'ghw':
                    graphemes[i] = 'ghhw'

    #Rule 2)
    for i in range(0, len(graphemes)):
        if graphemes[i] in doubleable_nasal:
            if i > 0 and graphemes[i-1] in unvoiced_consonants_nd:
                if graphemes[i] == 'n':
                    graphemes[i] = 'nn'

                elif graphemes[i] == 'm':
                    graphemes[i] = 'mm'

                elif graphemes[i] == 'ng':
                    graphemes[i] = 'ngng'

                elif graphemes[i] == 'ngw':
                    graphemes[i] = 'ngngw'

    #Rule 3a)
    for i in range(0, len(graphemes)):
        if graphemes[i] in doubleable_fricative or graphemes[i] in doubleable_nasal:
            if i > 0 and graphemes[i-1] in unvoiced_fricative_doubled:
                if graphemes[i] == 'l':
                    graphemes[i] = 'll'

                elif graphemes[i] == 'r':
                    graphemes[i] = 'rr'

                elif graphemes[i] == 'g':
                    graphemes[i] = 'gg'

                elif graphemes[i] == 'gh':
                    graphemes[i] = 'ghh'

                elif graphemes[i] == 'ghw':
                    graphemes[i] = 'ghhw'

                elif graphemes[i] == 'n':
                    graphemes[i] = 'nn'

                elif graphemes[i] == 'm':
                    graphemes[i] = 'mm'
        
                elif graphemes[i] == 'ng':
                    graphemes[i] = 'ngng'

                elif graphemes[i] == 'ngw':
                    graphemes[i] = 'ngngw'

    #Rule 3b)
    for i in range(0, len(graphemes)):
        if graphemes[i] in doubleable_fricative or graphemes[i] in doubleable_nasal:
            if i != len(graphemes)-1 and graphemes[i+1] == 'll':
                if graphemes[i] == 'l':
                    graphemes[i] = 'll'

                elif graphemes[i] == 'r':
                    graphemes[i] = 'rr'

                elif graphemes[i] == 'g':
                    graphemes[i] = 'gg'

                elif graphemes[i] == 'gh':
                    graphemes[i] = 'ghh'

                elif graphemes[i] == 'ghw':
                    graphemes[i] = 'ghhw'

                elif graphemes[i] == 'n':
                    graphemes[i] = 'nn'

                elif graphemes[i] == 'm':
                    graphemes[i] = 'mm'

                elif graphemes[i] == 'ng':
                    graphemes[i] = 'ngng'

                elif graphemes[i] == 'ngw':
                    graphemes[i] = 'ngngw'

    for i in range(0, len(graphemes)): 
        ret = ret + graphemes[i]

    return ret


def main():
    for input_sent in stdin:
        words = nltk.word_tokenize(input_sent)
        words = [str.lower(word.strip('.').strip(':').strip(',')) for word in words]
        for word in words:
            graphemes = tokenize(word, True)
            devoiced = apply_devoicing(graphemes)
            print(devoiced, end = ' ')
        print('\n', end = '')


if __name__ == "__main__":
    main()

else: 
    exit
