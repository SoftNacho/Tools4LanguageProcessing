=======================
Homework for LING 402
=======================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Part 2 (13%)
===========

Implement the body of c.py so that it produces the same output as that found in expected_output/c when run on data/hansards1000.tsv

That data file is a parallel text of French and English sentences, with one sentence pair per line. Each line consists of the French sentence, followed by a tab, followed by the English sentence.

The program should first ensure that the user has provided exactly one command line argument. If not, the program should fail with a usage message of the format "Usage:\t{} file", where {} is replaced by the name of the program (you may not hard code the name in the string).

The program should then read the file. The program should tokenize each sentence using nltk.word_tokenize. The program should count the number of lines, the total number of tokens on the English side of the corpus, and the total number of tokens on the French side of the corpus.

Finally, the program should print the average number of French tokens per line, then a newline, then the average number of English tokens per line, then a newline.

