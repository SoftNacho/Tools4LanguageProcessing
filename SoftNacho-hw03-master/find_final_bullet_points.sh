#!/bin/bash

###############################################################################
# Instructions:
###############
#
# The file /usr/share/emacs/24.3/etc/WHY-FREE contains a number of lines
# that contain bullet points (lines that begin with *)
#
# Modify this script so that it prints the final three bullet point lines
# (and nothing else)
#
#
# HINT: You will likely need to two commands connected with a pipe
#
###############################################################################



grep "* [A-Z]" /usr/share/emacs/24.3/etc/WHY-FREE |tail -n3
