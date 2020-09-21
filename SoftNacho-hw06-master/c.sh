#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/c.rst
#
###############################################################################


if [ -e $1 ]
then 
	rm -rf $1
fi

mkdir $1

for i in January February March April May June July August September October November December; do

	mkdir $1/$i 
	
	#switch case here
	case $i in  
		January)
		for j in $(seq 1 31); do touch $1/$i/$j ;done
		;;
		
		February)
		for j in $(seq 1 28); do touch $1/$i/$j; done
		;;

		March)
		for j in $(seq 1 31); do touch $1/$i/$j; done
		;;

		April)
		for j in $(seq 1 30); do touch $1/$i/$j; done
		;;

		May)
		for j in $(seq 1 31); do touch $1/$i/$j; done
		;;

		June)
		for j in $(seq 1 30); do touch $1/$i/$j; done
		;;

		July)
		for j in $(seq 1 31); do touch $1/$i/$j; done
		;;
	
		August)
		for j in $(seq 1 31); do touch $1/$i/$j; done
		;;
			
		September)
		for j in $(seq 1 30); do touch $1/$i/$j; done
		;;

		October)
		for j in $(seq 1 31); do touch $1/$i/$j; done
		;;

		November)
		for j in $(seq 1 30); do touch $1/$i/$j; done
		;;

		December)
		for j in $(seq 1 31); do touch $1/$i/$j; done
		;;
	esac
done






