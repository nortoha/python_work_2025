# Holly Norton
# Given 2 strings, a and b, return a string of the form 
# short+long+short, with the shorter string on the outside 
# and the longer string on the inside. 
# The strings will not be the same length, but they may be empty (length 0).

a = "Hello"
a_len = len(a)
# print(a_len)

b = "hi"
b_len = len(b)
# print(b_len)

if a_len>b_len:
    print(b + a + b)
else:
    print(a + b + a)