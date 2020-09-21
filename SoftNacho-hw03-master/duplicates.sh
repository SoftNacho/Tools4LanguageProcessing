#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it prints to standard output 
#  a listing of those file names that are found in both /bin and /usr/bin
#
# NOTE:
#
#  The listing must list exactly one file name per line (and nothing else),
#  and must be sorted alphabetically.
#
# 
# HINT: Make sure you have read Chapter 6 of the command line textbook
#
###############################################################################



ls /bin /usr/bin/ | uniq -i -D | sort
