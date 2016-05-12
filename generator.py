#!/usr/local/bin/python3

# This file was created on 11/05/2016
# Author: George Kaimakis

# generator tutorial from Corey Schafer's Python Tutorial Series

#def square_numbers (nums):
#    for i in nums:
#        yield (i * i)

#my_nums = square_numbers ([1,2,3,4,5])

my_nums = (x * x for x in [1,2,3,4,5])

print ()
print (list(my_nums))
print ()

#    print (next(my_nums))  # [1, 4, 9, 16, 25]

#    print ()
#    for num in my_nums:
#        print (num)
#    print ()

