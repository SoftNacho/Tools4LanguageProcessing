#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input,
#  replacing every sequence of one or more whitespace characters 
#  (including at least the following: space, tab, newline) 
#  with a single newline character,
#  printing the result to standard output
#
###############################################################################



echo "Welcome to whitespace: press ctrl+D when done typing" ; tee | tr '\t' '\n' | tr " " '\n' | sed '/^\s*$/d'
