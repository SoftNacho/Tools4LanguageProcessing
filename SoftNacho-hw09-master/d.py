#!/usr/bin/python3

import nltk.corpus as corpus
from nltk.corpus import udhr

count = 0

for fileid in udhr.fileids():
	count += 1
	
	print('{0:03d}'.format(count), fileid)
