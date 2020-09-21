#!/usr/bin/python3

import nltk.corpus as corpus
from nltk.corpus import gutenberg

for fileid in gutenberg.fileids():
	sentence = len(gutenberg.sents(fileid))
	words = len(gutenberg.words(fileid))
	avg = words / sentence

	print(fileid, avg)
