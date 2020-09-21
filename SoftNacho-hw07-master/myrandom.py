#!/usr/bin/python3
import random

############################################
#__Helper function for rock paper scissor__#
#                                          #
#Generates a random number between 1 and 3.#
############################################
def rock_paper_scissors():
        rps=random.randint(1,3)

        if rps == 1:
                return "rock"

        elif rps == 2:
                return "paper"

        elif rps == 3:
                return "scissors"
############################################
#__Helper function for chutes and ladders__#
#					   #
#Generates a random number between 1 and 6.#
############################################
def chutes_and_ladders_spinner():
	spin=random.randint(1,6)
	
	return spin
