=======================
Homework 4 for LING 402
=======================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Part 3 (15%)
===========

First, complete `Part 2`_.
 
After successfully implementing c.sh, you should start implementing b.sh 
by copying the body of c.sh into b.sh. 
Then, implement the new instructions, which are in bold below.
Instructions not in bold are from `Part 2`_.

* **Check the number of positional parameters that were supplied as arguments.**
  **If that number is less than 1 or greater than 1, the script should echo the following message:**

  **"Usage: $0 year", and then should exit**
    
    
* Bash will automatically store the first positional parameter as $1

  If a directory within the present working directory 
  exists with that name (the name of the supplied year),
  delete that directory and its contents.


* Create a directory within the present working directory
  with the name of the first positional parameter (the name of the supplied year)


* Use a traditional shell form for-each loop to do the following:

  Within the year directory, create one directory for each month.

  Use the full names of each month, with the first letter capitalized:
  
  - January
  - February
  - March
  - April
  - May
  - June
  - July
  - August
  - September
  - October
  - November
  - December


* Within the for loop, use bash switch-case statements
  to determine which month you is currently being handled in the loop.
   
  **You will only have 3 cases:**
  - **one case for months with 31 days,**
  - **one case for months with 30 days,**
  - **one case for February**


* Within each case, use the $( ) notation, the seq command,
  and a for-each loop to iterate over the days of the month.

* Within each month's for-each loop, for each day use touch to create an empty file
  named after each day of the current month.
   
  These files should be created within the appropriate month's directory.

* **In this script, assume that February has 28 days,**
  **except in years that are evenly divisible by 4, when Febrary has 29 days.**



Reference
=========

You may find it helpful to refer to the following sections of `The Linux Command Line: A Complete Introduction`_:
 
* In Chapter 27, the section titled "Using if"

* In Chapter 27, the section titled "Integer Expressions"

* In Chapter 31, the section titled "Combining Multiple Patterns"

  Important note: You should **not** use the read statement in this assigment



.. _`Part 2`: c.rst
.. _`The Linux Command Line: A Complete Introduction`: http://proquest.safaribooksonline.com.proxy2.library.illinois.edu/book/programming/linux/9781593273897
