#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it creates a directory called months.
#
# Within the months directory, your script should create one directory
#  for each year in 2010 through 2016.
#
# Within each year directory, your script should create one directory
#  for each month (01 through 12)
#
#
# IMPORTANT: You may only use one command to do the above. 
#
#
# NOTE:
#
# After running this script successfully, running the following command
#  should produce the following result:
#
# $ ls months/*
# months/2010:
# 01  02  03  04  05  06  07  08  09  10  11  12
#
# months/2011:
# 01  02  03  04  05  06  07  08  09  10  11  12
#
# months/2012:
# 01  02  03  04  05  06  07  08  09  10  11  12
#
# months/2013:
# 01  02  03  04  05  06  07  08  09  10  11  12
#
# months/2014:
# 01  02  03  04  05  06  07  08  09  10  11  12
#
# months/2015:
# 01  02  03  04  05  06  07  08  09  10  11  12
#
# months/2016:
# 01  02  03  04  05  06  07  08  09  10  11  12#
# 
#
#
# HINT: Make sure you have read Chapter 6 of the command line textbook
#
###############################################################################



mkdir -p months/201{0..6}/{01..12}
