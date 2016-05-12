#!/usr/local/bin/python3

# This file was created on 11/05/2016
# Author: George Kaimakis

# generator tutorial from Corey Schafer's Python Tutorial Series

def square_numbers (nums):
    result = []
    for i in nums:
        result.append (i * i)
    return result

my_nums = square_numbers ([1,2,3,4,5])

print ()
print (my_nums)  # [1, 4, 9, 16, 25]
print ()

