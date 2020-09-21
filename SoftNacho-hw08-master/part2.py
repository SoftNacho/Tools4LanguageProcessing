#!/usr/bin/python3

from sys import stdin


# Iterate over each line of standard input
for input_line in stdin:

    # Remove leading and trailing whitespace
    input_line.strip()
    
    # Remove leading and trailing parens
    input_line.strip("(")
    input_line.strip(")")

    # Remove leading and trailing whitespace
    input_line.strip()

    # Print the output_line
    output_line = input_line
    print(output_line)
