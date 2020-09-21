=======================
Homework 4 for LING 402
=======================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Part 2 (15%)
===========

First, complete `Part 1`_.
 
After successfully implementing d.sh, you should start implementing c.sh 
by copying the body of d.sh into c.sh. 
Then, implement the new instructions, which are **in bold** below.
Instructions not in bold are from `Part 1`_.

    
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


* **Within the for loop, use bash switch-case statements**
  **to determine which month you is currently being handled in the loop.**
   
  **You will have 12 cases, one for each month.**


* **Within each case, use the $( ) notation, the seq command,**
  **and a for-each loop to iterate over the days of the month.**

* **Within each month's for-each loop, for each day use touch to create an empty file**
  **named after each day of the current month.**
   
  **These files should be created within the appropriate month's directory.**

* **In this script, assume that February always has 28 days.**



Reference
=========

You may find it helpful to refer to the following sections of `The Linux Command Line: A Complete Introduction`_:
 
* In Chapter 7, the section titled "Command Substitution"

* In Chapter 31, everything before the section titled "Combining Multiple Patterns"

  Important note: You should **not** use the read statement in this assigment



.. _`Part 1`: d.rst
.. _`The Linux Command Line: A Complete Introduction`: http://proquest.safaribooksonline.com.proxy2.library.illinois.edu/book/programming/linux/9781593273897
