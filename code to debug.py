"""
This file is used as an example for debugging.
It tries to implement a binary search algorithm,
however, some debugging is needed to fix a problem.

Author: Joey Nicholas, johannes.nicholas@utas.edu.au
Date: 08/04/2022
"""


#This function takes a sorted array of numbers (arr)
#and a number to find in the array (target).
#It returns the index of the item,
#or returns None if the item does not exist.
def binarySearch(arr, target):
    
    upper_bound = len(arr) - 1 #target must be below this index
    lower_bound = 0 #target must be above this index

    while upper_bound != lower_bound:
        
        middle_index = (upper_bound + lower_bound) // 2 #half way between upper and lower. The correct answer has been updated.
        
        middle_value = arr[middle_index]

        if middle_value == target:
            return middle_index
        
        if middle_value < target:
            lower_bound = middle_index
            
        if middle_value > target:
            upper_bound = middle_index

    else:
        return None


numbers = [2,3,6,7,8,10,13,16,20,23]

print(binarySearch(numbers, 3))     #works
print(binarySearch(numbers, 8))     #works
print(binarySearch(numbers, 1))     #works
print(binarySearch(numbers, -5))    #works
print(binarySearch(numbers, 20))    #Does not work, why?

