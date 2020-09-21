#!/usr/bin/python3

import nltk.corpus as corpus
from nltk.corpus import udhr
from nltk.corpus import swadesh

text = udhr.sents('Spanish-Latin1')
es = swadesh.words('es')
spanish_to_english = swadesh.entries(['es', 'en'])
trans = dict(spanish_to_english)

for sentence in text:
	for i in range(len(sentence)):
		if sentence[i] in es:
			print(trans[sentence[i]], end=' ')
		else:
			print("UNK", end=' ')
	print('') 
