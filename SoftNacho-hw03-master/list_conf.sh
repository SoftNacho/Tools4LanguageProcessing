#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it prints to standard output 
#  a listing of all files in the /etc directory that end in the suffix .conf
#
# NOTE:
#
#  The listing:
#    * must print the allocated size of each file, in blocks
#    * must list exactly one file per line
#    * must NOT be in long format (as described by the ls man page)
#
# For example, the beginning of your listing should look like this:
#
#  4 /etc/adduser.conf
#  4 /etc/blkid.conf
# 12 /etc/ca-certificates.conf
#  4 /etc/colord.conf
#
###############################################################################



ls /etc/ | grep -b ".conf$" | sed 's/:/ /'
