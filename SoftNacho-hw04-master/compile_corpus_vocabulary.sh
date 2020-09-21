#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input,
#  and prints (to standard output) a list of the unique words present in the input.
#
# Output should be printed with one word per line.
#
# Do not output any lines that consist entirely of whitespace.
#
# Output must be sorted in alphabetical order 
#  (so, for example, the word "any" should be printed before the word "zebra")
#
# HINT: You will likely need to pipe together multiple commands.
#
###############################################################################


echo "Welcome to 'compile corpus': press enter and ctrl+D when done typing" ; cat | tr " " '\n' | sort -df | uniq -i

#read | sort -d -f | uniq 

#echo "Welcome to unique words: press ctrl+D when done typing" ; cat > temp.txt ; sort temp.txt > temp.txt | uniq temp.txt > temp.txt | less
