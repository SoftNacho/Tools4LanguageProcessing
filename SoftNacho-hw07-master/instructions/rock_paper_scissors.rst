=====================
Homework for LING 402
=====================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


In myrandom.py:

* Create a function called rock_paper_scissors.  In this function, generate a random number (with possible values of 1, 2, or 3). If the value is 1, return the string "rock". Otherwise, if the value is 2, return the string "paper". Otherwise, if the value is 3, return the string "scissors".


Implement the body of rock_paper_scissors.py:

* Import myrandom

* Create a function called main. This function should call your rock_paper_scissors function and print the result.

* Outside function, in the body of your script, test to see if the special variable called __name__ has the value "__main__". If it does, call your main() function.

* The result should be that if you execute your script from the command line (./rock_paper_scissors.py), the program should print one of the values: rock, paper, or scissors. But, if someone were to import your rock_paper_scissors.py file as a module, the main function in rock_paper_scissors.py should not automatically execute.

