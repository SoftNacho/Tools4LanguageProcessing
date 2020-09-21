#!/usr/bin/python3

from sys import stdin

class Node:
    def __init__(self,string,level):
        self.string=string
        self.level=level



# Iterate over each line of standard input
for line in stdin:

    # Split the line on whitespace into parts
    parts = line.split()

    # Create an empty list called parents
    parents = []

    # Create an empty list called children
    children = []

    # Create a variable called level, initially set to 0
    level = 0

    # Iterate over each part in parts
    for part in parts:

        # If the part starts with an opening paren
        if part[0] == "(":
            
            # Increment the level
            level += 1

            # Obtain the parent_string by stripping off the opening paren
            parent_string = part.strip("(")

            # Create a new node using the parent_string and the current level
            new_node = Node(parent_string, level)

            # Append that new node to the end of the parents list
            parents.append(new_node)

        #length = len(part)
        # Otherwise, if the part ends with a closing paren
        elif part[len(part)-1] == ")":

            # Obtain the child_string by stripping off the closing paren
            child_string = part.strip(")")

            # Get the parent_node by popping it off the end of the parents list
            parent_node = parents.pop() 

            # If the child_string is not empty
            if child_string != "":

                # Print an output line, using the format string "{}\t{}", 
                #       where the first slot is the child_string
                #       and the second slot is the string of the parent_node
                print(child_string, "\t", parent_node)
            else:

                # Get the child_node by popping off the end of the children list
                child_node = children.pop()

                # Get the string of the child_node
                child_string = child_node.string 

                # While the length of the children list is greater than zero,
                #       and the level of the last entry in the children list
                #       is the same as the level of child_node
                while (len(children) != 0 and children[len(children)-1].level == child_node.level):
                    
                    # Get the previous_child_node by popping off the end of the children list
                    previous_child_node = children.pop()

                    # Set the value of children_string using the format string "{} {}",
                    #     where the first slot is the string of the previous_child_node,
                    #     and the second slot is the current value of children_string
                    children_string = "{} {}".format(previous_child_node.string, child_string)

                # Print an output line, using the format string "{}\t{}", 
                #       where the first slot is the children_string
                #       and the second slot is the string of the parent_node
                print(children_string, "\t", parent_node)

            # Append the current parent_node to the end of the children list
            children.append(parent_node)

            # Decrement the value of level
            level -= 1

        # We should never reach this else clause
        else:

            # Raise a RuntimeError with the following message "Reached a part of the code that should be unreachable"
            print("Reached a part of the code that should be unreachable")
