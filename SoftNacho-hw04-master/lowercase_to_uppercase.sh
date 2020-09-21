#/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input
#  transliterates the text to all upper-case, 
#  printing the resulting text to standard output
#
###############################################################################


echo "Welcome to 'lower to upper': Press ctrl+D once done writing"; tee | tr "[:lower:]" "[:upper:]"
