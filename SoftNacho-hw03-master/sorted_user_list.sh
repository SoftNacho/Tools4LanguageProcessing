#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it transforms the contents of the file /etc/passwd
#  into a list of usernames (one username per line), sorted alphabetically,
#  printing the output to standard output.
#
###############################################################################



cat /etc/passwd | sort | cut -d':' -f1
