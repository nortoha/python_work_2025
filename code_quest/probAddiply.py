# Recommended imports for all problems
# Some problems may require more
import sys
import math
import string

# Always start with reading in the number
# of test cases from standard input. The
# rstrip() method removes the lingering newline
cases = int(sys.stdin.readline().rstrip())
# Loop for each test case. This is the last line
# common to all problems; the content of this
# loop will change based on the problem solved.
for caseNum in range(cases):
	# For problem B, we need to read in our data
	# this line of code will be in every one of your answers because
	# this is how we read data from the console (aka. standard input channel)
	dataString = sys.stdin.readline()
	# take that line and split it by the colon character.  this will give
	# us an array with index 0 being the first value and index 1 being the second value
	data = dataString.split(" ")
	# create variables and convert it to float numbers since the problem said they were decimals
	num1 = int(data[0])
	num2 = int(data[1])
	
    # print the sum, space, print the product
	sum = num1 + num2
	product = num1 * num2
	print(sum, " ", product)
