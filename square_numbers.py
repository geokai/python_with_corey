# square_numbers:
# This file was created on 14/07/17
# Author: George Kaimakis

# this code taken from Corey Schafer's 'generator' tutorial:

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)
