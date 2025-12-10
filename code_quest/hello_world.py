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
        # For problem A, we're just spitting out
        # the input as it's written
        print(sys.stdin.readline().rstrip())
