=====================
Homework for LING 402
=====================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


In this part you will implement the children's board game "Chutes and Ladders"

If you are not familiar with the game, an image of the board is included here as chutes_and_ladders.gif, the rules are described here: https://www.hasbro.com/common/instruct/ChutesandLadders.PDF

In myrandom.py:

* Create a function called chutes_and_ladders_spinner. In this function, generate a random number with possible values of 1, 2, 3, 4, 5, or 6. Return the result.


In chutes_and_ladders.py:

* Import myrandom

* Create a function called move. This function should have two parameters. The first parameter should be called starting_space. This represents a player's position on the board (the squares are numbered 1-100. Before the game starts a player's position would be 0). The second parameter should be called distance (This will represent the result of the player spinning the spinner, which is numbered 1-6). You can assume that these parameters will always have non-negative integer values. Your function should add the two parameters together to determine the player's new position. Players in the game have to land exactly on the 100 square to win; therefore, if the calculated new position is greater than 100, ignore the distance parameter and set the new position to starting_space. After calculating the new position, you need to check to see if that new position is at the bottom of a ladder (squares 1, 4, 9, 28, 36, 51, 71, 80) - if so, the new position should be the square at the top of the ladder; or if the new position is at the top of a slide (squares 16, 47, 49, 56, 62, 64, 87, 93, 95, 98) - if so, the new position should be the square at the bottom of the slide. Finally, return the calculated new position.

* Create a function called play_chutes_and_ladders. This function should take a single parameter called print. You can assume that this parameter will always be a boolean value. This function should have a variable called current_position, which should initially be set to zero. Create a while loop. The while loop should execute until current_position has the value 100. Inside the loop, call chutes_and_ladders_spinner to get a number between 1 and 6. Call function move, passing the current position and your newly generated random number. If the print variable supplied to this function has a value of true, print "X\tY\tZ", where X is the current_position before the move, Y is the random number that you generated, Z is the new position, and \t is a tab character. Update current_position to be the result of calling move. At the end of the function, return the number of moves that were performed.

* Outside your two functions, in the body of your script, test to see if the special variable called __name__ has the value "__main__". If it does, call your play_chutes_and_ladders() function.

* The result should be that if you execute your script from the command line (./chutes_and_ladders.py), the program should print the results of playing one single-player game of chutes and ladders, with each move printed on a separate line. But, if someone were to import your chutes_and_ladders.py file as a module, the main function in chutes_and_ladders.py should not automatically execute.

