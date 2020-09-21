#!/usr/bin/python3

from sys import stdin

#counts used for end of tree check
#open_count = 0
#close_count = 0

# Create a new variable called level, with an inial value of 0
level = 0

# Create a new variable called output_line, with an initial value of ""
output_line = ""

# Iterate over each line of standard input
for input_line in stdin:

    # Remove leading and trailing whitespace from the input_line
    input_line.strip()
    input_line.strip('\n')
    # If the stripped line is not empty
    if input_line != "": 

        # Insert a space before each opening paren in the line
        input_line.replace('(', ' (')
       
	# Insert a space after each closing paren in the line
        input_line.replace(')', ') ')
	
        # Increment level for each opening paren
        for i in range(len(input_line)):
            if input_line[i] == '(':
                level += 1	

        # Decrement level for each closing paren
        for i in range(len(input_line)):
            if input_line[i] == ')':
                level -= 1

        # Append the current line to the output_line
        output_line += input_line

        # If we have read the entire tree
        if level == 0:

            # Print output_line
            print(output_line)

            # And reset the output_line variable to an empty string
            output_line = ""
