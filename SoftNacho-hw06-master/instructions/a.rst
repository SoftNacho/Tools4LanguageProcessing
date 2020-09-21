=======================
Homework 4 for LING 402
=======================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Part 4 (15%)
===========

First, complete `Part 3`_.
 
After successfully implementing b.sh, you should start implementing a.sh 
by copying the body of b.sh into a.sh. 
Then, implement the new instructions, which are in bold below.
Instructions not in bold are from `Part 3`_.

* Check the number of positional parameters that were supplied as arguments.
  If that number is less than 1 or greater than 1, the script should echo the following message:

  "Usage: $0 year", and then should exit
    
    
* **The first positional parameter should be a four-digit year.**

  **If the first positional parameter isn't a four-digit year, the script should echo the following message:**
  
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
   
  You will only have 3 cases:
  - one case for months with 31 days,
  - one case for months with 30 days,
  - one case for February


* Within each case, use the $( ) notation, the seq command,
  and a for-each loop to iterate over the days of the month.

* **Within the for-each loop, use wget to download the English Wikipedia**
  **page for the given day in the given month.**

  **You must download the printable version of the relevant pages.**

  **For example, the URL for February 15 is**
  **http://en.wikipedia.org/w/index.php?title=February_15&printable=yes**

  **As in the other scripts, these files should be placed in the appropriate**
  **month directory, and the filename should simply be the day of the month.**

* **In this script, you must correctly calculate when February has 28 days,**
  **and when Febrary has 29 days, according to the following:**

  - **If the year is evenly divisible by 400, February has 29 days**
  - **Otherwise, if the year is evenly divisible by 100, February has 28 days**
  - **Otherwise, if the year is evenly divisible by 4, February has 29 days**
  - **Otherwise, February has 28 days**
  

Reference
=========

You may find it helpful to refer to the following sections of `The Linux Command Line: A Complete Introduction`_:
 
* In Chapter 27, the section titled "Using if"

* In Chapter 27, the section titled "Integer Expressions"

* In Chapter 27, the section titled "A More Modern Version of test"

* In Chapter 32, the section titled "Accessing the Command Line"


.. _`Part 3`: b.rst
.. _`The Linux Command Line: A Complete Introduction`: http://proquest.safaribooksonline.com.proxy2.library.illinois.edu/book/programming/linux/9781593273897
