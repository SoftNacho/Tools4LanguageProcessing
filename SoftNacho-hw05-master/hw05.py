#!/usr/bin/python3
#
# In the space below, write a Python program.
#
# The program should prompt the user with the following message:
# "Please enter an integer representing a number of seconds: "
#
# The program should then print a message
#   converting the specified number of seconds into Weeks, Days, Hours, Minutes, and Seconds.
#
# For example, if the user runs the program and, when prompted, enters 917837, the result should be:
# weeks= 1 days= 3 hours= 14 minutes= 57 seconds= 17

 

user_int = int( input ('Please enter an integer representing a number of seconds: '))
  
weeks = user_int//604800
left_weeks = user_int%604800
  
days = left_weeks//86400
left_days = left_weeks%86400
  
hours = left_days//3600
left_hours = left_days%3600
  
minutes = left_hours//60
  
seconds = left_hours%60
 
print ("weeks=", weeks, "days=", days,  "hours=", hours, "minutes=", minutes, "seconds=", seconds)


