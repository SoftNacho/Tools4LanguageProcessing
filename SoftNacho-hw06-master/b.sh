#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/b.rst
#
###############################################################################


if [[ $# < 1 || $# > 1 ]]
then
        echo Usage $0 year
        exit 
fi    

if [ -e $1 ]
then 
	rm -rf $1
fi

mkdir $1

for i in January February March April May June July August September October November December; do

	mkdir $1/$i 
	
	#switch case here
	case $i in  
		#Months with 31 days
		January|March|May|July|August|October|December) 
		for j in $(seq 1 31); do touch $1/$i/$j ;done
		;;
		
		#Months with 30 days
		April|June|September|November)
		for j in $(seq 1 30); do touch $1/$i/$j; done
		;;
	
		#February
		February)
		remainder=$(($1 % 4)) 
		if [ $remainder = 0 ] 
                then	
			for j in $(seq 1 29); do touch $1/$i/$j; done
		else 
			for j in $(seq 1 28); do touch $1/$i/$j; done
		fi
                ;;
	esac
done






