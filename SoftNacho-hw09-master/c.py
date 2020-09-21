#!/usr/bin/python3

import nltk.corpus as corpus
from nltk.corpus import udhr

for fileid in udhr.fileids():
	words = len(udhr.words(fileid))	
	unique = len(set(udhr.words(fileid)))
	
	print(fileid, words, unique)
