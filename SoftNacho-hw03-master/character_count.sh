#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it prints the number of characters
# in the file /usr/share/emacs/24.3/etc/WHY-FREE (and nothing else).
#
# IMPORTANT NOTE: Your script should ONLY print the number of characters.
#                 It should NOT also print the file name.
#
#
# HINT: You will likely need to use either a pipe or a redirect operator
#
###############################################################################


wc -m /usr/share/emacs/24.3/etc/WHY-FREE | cut -d' ' -f1
