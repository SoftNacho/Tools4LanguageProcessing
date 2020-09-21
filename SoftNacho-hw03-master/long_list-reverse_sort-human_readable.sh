#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it prints to standard output 
#  a listing of the contents of the root directory.
#
# NOTE:
#
#  The listing must be in long format (as described by the ls man page)
#
#  The listing must be sorted in reverse date order, 
#      such that the oldest files are listed at the top of the listing
#      and the newest files are listed at the bottom of the listing
#
#  The file sizes in the listing must be in human-readable format (as described by the ls man page)
#
###############################################################################



ls -l -h -r -t /
