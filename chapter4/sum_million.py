# using for loop to the_sum
the_sum = 0
for n in range(1, 1000001):
    #the_sum = the_sum + n
    the_sum+=n
print(f"The sum of the first million integers is {the_sum}.")

# making a list to sum
the_sum = 0 # reset the the_sum variable
numbers = list(range(1,1000001))
for n in numbers:
    the_sum+=n
print(f"The sum using a list and loop is {the_sum}.")

# using the sum function (this is the most efficient way)
print(sum(numbers))

