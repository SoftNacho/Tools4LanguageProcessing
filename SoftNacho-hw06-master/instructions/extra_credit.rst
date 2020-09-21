=======================
Homework 4 for LING 402
=======================

--------------------------------------------------------
Tools and Techniques for Speech and Language Processing
--------------------------------------------------------


Optional Part 5 (5%)
=====================

First, complete `Part 4`_.
 
After successfully implementing a.sh, you should start implementing extra_credit.sh 
by copying the body of a.sh into extra_credit.sh. 
Then, implement the new instructions, which are in bold below.
Instructions not in bold are from `Part 4`_.

* Check the number of positional parameters that were supplied as arguments.
  If that number is less than 1 or greater than 1, the script should echo the following message:

  "Usage: $0 year", and then should exit
    
    
* The first positional parameter should be a four-digit year.

  If the first positional parameter isn't a four-digit year, the script should echo the following message:
  "Usage: $0 year", and then should exit
    
    
* Bash will automatically store the first positional parameter as $1

  If a directory within the present working directory 
  exists with that name (the name of the supplied year),
  delete that directory and its contents.


* Create a directory within the present working directory
  with the name of the first positional parameter (the name of the supplied year)


* **Within the year directory, use a C-style for loop to create one directory for each month.**

  **Use the date command to determine the full names of each month for the current locale.**


* **Within the for loop, use ncal to determine what days are present**
  **for the given month in the given year**
   
  **You may not use any if statements or case statements**

* **Use a for-each loop to iterate over the days of the month.**

* Within the for-each loop, use wget to download the English Wikipedia
  page for the given day in the given month.

  You must download the printable version of the relevant pages.

  For example, the URL for February 15 is
  http://en.wikipedia.org/w/index.php?title=February_15&printable=yes

  As in the other scripts, these files should be placed in the appropriate
  month directory, and the filename should simply be the day of the month.



.. _`Part 4`: a.rst
.. _`The Linux Command Line: A Complete Introduction`: http://proquest.safaribooksonline.com.proxy2.library.illinois.edu/book/programming/linux/9781593273897
