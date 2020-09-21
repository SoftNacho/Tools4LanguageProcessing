#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it prints to standard output 
#  a listing of all files in the /usr/bin directory whose names begin with f and whose names are exactly 4 characters long
#
# NOTE:
#
#  The listing:
#    * must list exactly one file per line
#    * must NOT be in long format (as described by the ls man page)
#
# 
# HINT: This script can be completed without using pipes
#
###############################################################################



ls /usr/bin/ | grep "^f...$"
