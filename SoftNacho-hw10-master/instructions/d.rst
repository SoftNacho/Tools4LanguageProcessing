=======================
Homework for LING 402
=======================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Part 1 (61%)
===========

Implement the body of d.py so that it produces the same output as that found in expected_output/d when run on data/hansards1000.tsv

That data file is a parallel text of French and English sentences, with one sentence pair per line. Each line consists of the French sentence, followed by a tab, followed by the English sentence.

The program should first ensure that the user has provided exactly one command line argument. If not, the program should fail with a usage message of the format "Usage:\t{} file", where {} is replaced by the name of the program (you may not hard code the name in the string).

The program should then read the file, and for each line, the program should print the English sentence, followed by a tab, followed by the French sentence.
