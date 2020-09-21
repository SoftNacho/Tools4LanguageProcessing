#!/usr/bin/python3
from d import tokenize
from c import apply_devoicing
from sys import stdin
import nltk
# PART B (10%)
#
# Implement the graphemes2ipa function.
# It should accept a list of graphemes, and return a list of IPA symbols.
# If any grapheme is not a Yupik letter, it should be passed through unchanged.
#
# When this file is executed, it should:
#     * accepts text from standard input,
#     * lowercases it, 
#     * tokenizes it into Yupik graphemes using your tokenize function from d.py (with keep_apostrophes=False),
#     * applies the automatic devoicing rules using your apply_devoicing function from c.py, 
#     * converts each grapheme into the appropriate IPA symbol using your graphemes2ipa function,
#     * and then print the corresponding output (formatted as words, not lists of graphemes).
#
# You will need to import tokenize from d.py
# You will need to import apply_devoicing from c.py
#
# Your output should not contain any apostrophes.

def graphemes2ipa(graphemes):
    #creating dict for IPA symbols
    letterToIPA = {"i":"i", "a": "ɑ", "u":"u", "e":"ə", 
                   "p":"p", "t":"t", "k":"k", "kw":"kʷ", "q":"q", "qw":"qʷ",
                   "v":"v", "l":"ɮ", "z":"z", "y":"j", "r":"ʐ", "g":"ɣ", "w":"ɣʷ", "gh":"ʁ", "ghw":"ʁʷ",
                   "f":"f", "ll":"ɬ", "s":"s", "rr":"ʂ", "gg":"x", "wh":"xʷ", "ghh":"χ", "ghhw":"χʷ", "h":"h",
                   "m":"m", "n":"n", "ng":"ŋ", "ngw":"ŋʷ",
                   "mm":"m̥", "nn":"n̥", "ngng":"ŋ̊", "ngngw":"ŋ̊ʷ",
                   "\'":""} 
    
    fiveLetterGraphemes = ["ngngw"]
    fourLetterGraphemes = ["ghhw", "ngng"]
    threeLetterGraphemes = ["ghw", "ghh", "ngw"]
    twoLetterGraphemes = ["kw", "qw", "gh", "ll", "rr", "gg", "wh", "ng", "mm", "nn"]
    oneLetterGraphemes = ["i", "a", "u", "e", "p", "t", "k", "q", "v", "l", "z", "y", "r", "g", "w", "f", "s", "h", "m", "n"]

    apostrophe = ["\'"]

    start = 0
    end = len(graphemes)

    return_word = ""

    while start < end:
        if graphemes[start:start+5] in fiveLetterGraphemes:
            return_word = return_word + letterToIPA[graphemes[start:start+5]]
            start += 5

        elif graphemes[start:start+4] in fourLetterGraphemes:
            return_word = return_word + letterToIPA[graphemes[start:start+4]]
            start += 4

        elif graphemes[start:start+3] in threeLetterGraphemes:
            return_word = return_word + letterToIPA[graphemes[start:start+3]]
            start += 3

        elif graphemes[start:start+2] in twoLetterGraphemes:
            return_word = return_word + letterToIPA[graphemes[start:start+2]]
            start += 2

        elif graphemes[start] in oneLetterGraphemes:
            return_word = return_word + letterToIPA[graphemes[start]]
            start += 1

        elif graphemes[start] in apostrophe:
            return_word = return_word + letterToIPA[graphemes[start]]
            start += 1

        else:
            return_word = return_word + graphemes[start]
            start += 1


    return return_word


def main():
    for input_sent in stdin:
        words = nltk.word_tokenize(input_sent)
        words = [str.lower(word.strip('.').strip(':').strip(',')) for word in words]
        for word in words:
            graphemes = tokenize(word, True)
            devoiced = apply_devoicing(graphemes)
            IPAword = graphemes2ipa(devoiced)
            print(IPAword, end = ' ')
        print('\n', end = '')



if __name__ == "__main__":
    main()

else: 
    exit
