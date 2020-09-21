#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/d.rst
#
###############################################################################


if [ -e $1 ]
then 
	rm -rf $1
fi

mkdir $1

for i in January February March April May June July August September October November December; do mkdir $1/$i; done






