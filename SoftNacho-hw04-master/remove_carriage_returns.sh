#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input
#  and removes all carriage return characters,
#  printing the resulting text to standard output
#
# In other words, this script should convert text with MS-DOS style line endings
#    into text with Unix-style line endings
#
# HINT: The solution to this problem is discussed in the assigned reading
#
###############################################################################



echo "Welcome to DOS to Unix: press ctrl+D when done typing" ; cat | sed $'s/$/\r/'
