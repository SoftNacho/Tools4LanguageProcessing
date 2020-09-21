#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it takes text from standard input
#  performs spell check, and prints a list of misspelled words (one word per line)
#  to standard output
#
###############################################################################

echo "Welcome to 'spellcheck': Press ctrl+D once done writing"; tee | enchant -l
