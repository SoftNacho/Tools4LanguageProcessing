=====================
Homework for LING 402
=====================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Implement the body of simulate_rps.py:

* Import myrandom

* Create a function called main. This function should have a for loop iterates from 1 to 1000000. Each time through the loop, you should call your rock_paper_scissors function. Use variables to keep track of how many times each result (rock, paper, scissors) is returned. After your loop runs, print three lines that look like this:

R\trock
P\tpaper
S\tscissors

* In the above, R should be the number of times "rock" was returned, P should be the number of times "paper" was returned, and S should be the number of times "scissors" is returned.

* Outside your function, in the body of your script, test to see if the special variable called __name__ has the value "__main__". If it does, call your main() function.

* The result should be that if you execute your script from the command line (./simulate_rps.py), the program should print the results of playing one million single-player games of rock-paper-scissors, with the results printed at the end. But, if someone were to import your simulate_rps.py file as a module, the main function in simulate_rps.py should not automatically execute.

