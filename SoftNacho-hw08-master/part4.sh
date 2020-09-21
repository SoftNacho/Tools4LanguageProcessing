#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input
#  sorts the input,
#  then performs a uniq, counting the number of times each line occurs.
#
# The results should be printed to standard output in the form:
#
# count\tchildren\tparent
#
###############################################################################

sort | uniq -c | printf "%s\n" "$count\t$children\t$parent"

