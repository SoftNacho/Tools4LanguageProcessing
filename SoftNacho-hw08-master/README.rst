=====================
Homework for LING 402
=====================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Implement scripts to train a probabilistic context-free grammar.

All scripts must read from standard input and write to standard output.

1. Implement part1.py
  * The input to this script accepts parenthesized trees from the Wall Street Journal treebank in the mrg format 
  * The output from this script will be trees in the same parenthesized format, but one tree per line
2. Implement part2.py
  * The input to this script is the output of part1.py
  * The output from this script will be trees with leading and trailing whitespace removed, and with the extra set of parentheses removed
3. Implement part3.py
  * The input to this script is the output of part2.py
  * The output from this script will be rules
  * Unary rules will be in the following format: child<TAB>parent
  * Binary rules will be in the following format: child1<SPACE>child2<TAB>parent
  * Rules with more than 2 children will be in similar format, with children (separated by spaces), then a tab, then the parent
4. Implement part4.sh
  * The input to this script is the output of part3.py
  * The output will be sorted, first by children, then by parent
  * Lines will be in the following format: count<TAB>children<TAB>parent
5. Implement part5.py
  * The input to this script is the output of part4.sh
  * The output will be sorted, first by children, then by parent
  * Lines will be in the following format: probability<TAB>children<TAB>parent
