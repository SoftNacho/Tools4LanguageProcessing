#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input
#  and suppresses repeated empty lines,
#  printing the resulting text to standard output
#
###############################################################################



echo "Welcome to 'empty lines': Press enter followed by ctrl+D once done writing"; cat | awk 'NF' 
