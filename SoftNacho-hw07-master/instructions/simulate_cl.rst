=====================
Homework for LING 402
=====================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------



Implement the body of simulate_rps.py:

* Import chutes_and_ladders

* Create a function called main. This function should have a for loop iterates from 1 to 1000000. Each time through the loop, you should call your play_chutes_and_ladders - the print parameter should be set to false, so that results aren't printed. After your loop runs, print three lines that look like this:

X\tmin
Y\tmean
Z\tmax

* In the above, X should be the number of moves in the shortest simulated game, Y should be the mean number of moves over all of the simulated games, and Z should be the maximum number of moves in the longest simulated game.

* Outside your function, in the body of your script, test to see if the special variable called __name__ has the value "__main__". If it does, call your main() function.

* The result should be that if you execute your script from the command line (./simulate_cl.py), the program should print the results of playing one million single-player games of rock-paper-scissors, with the results printed at the end. But, if someone were to import your simulate_cl.py file as a module, the main function in simulate_cl.py should not automatically execute.

