#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/a.rst
#
###############################################################################

#makes sure only one arg
if [[ $# < 1 || $# > 1 ]]
then
        echo Usage $0 year
        exit 
fi    

#makes sure arg has length 4
if [[ $1 != ???? ]]
then 
	echo Usage $0 year
	exit
fi

#erases files with same name as arg
if [ -e $1 ]
then 
	rm -rf $1
fi

#creates dir with name arg
mkdir $1

#creates subdirs
for i in January February March April May June July August September October November December; do

	mkdir $1/$i 
	
	#switch case here
	case $i in  
		#Months with 31 days
		January|March|May|July|August|October|December) 
		for j in $(seq 1 31); do 
			wget -O $1/$i/$j -q http://en.wikipedia.org/w/index.php?title=${i}_${j}&printable=yes; 
		done
		;;
		
		#Months with 30 days
		April|June|September|November)
		for j in $(seq 1 30); do
			wget -O $1/$i/$j -q http://en.wikipedia.org/w/index.php?title=${i}_${j}&printable=yes;
		done
		;;
	
		#February
		February)
		remainder1=$(($1 % 400))
		remainder2=$(($1 % 100))
		remainder3=$(($1 % 4)) 
		#year divisible by 400
		if [ $remainder1 = 0 ] 
                then	
			for j in $(seq 1 29); do
				wget -O $1/$i/$j -q http://en.wikipedia.org/w/index.php?title=${i}_${j}&printable=yes;
			done
		
		#year divisible by 100
		elif [ $remainder2 = 0 ]
		then 
			for j in $(seq 1 28); do
				wget -O $1/$i/$j -q http://en.wikipedia.org/w/index.php?title=${i}_${j}&printable=yes;
			done
		
		#year divisible by 4
		elif [ $remainder3 = 0 ]
		then
			for j in $(seq 1 29); do
				wget -O $1/$i/$j -q http://en.wikipedia.org/w/index.php?title=${i}_${j}&printable=yes;
			done

		#other cases
		else
			for j in $(seq 1 28); do
				wget -O $1/$i/$j -q http://en.wikipedia.org/w/index.php?title=${i}_${j}&printable=yes;
			done
		fi
                ;;
	esac
done






