#/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it prints out a list of files located in /usr/bin
#   whose file names begin with an upper case letter and
#   for whom the remaining characters in the name are alphabetic characters.
#
# The printed list must be sorted,
#   must be printed with exactly one file per line
#   and the printed file names must NOT include the prefix /usr/bin
#
###############################################################################



ls /usr/bin/ | grep "^[A-Z]" | grep -v "[[:digit:]]" | grep -v "[[:punct:]]"
