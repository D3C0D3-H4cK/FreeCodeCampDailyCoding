"""
Symmetric Difference

Given two arrays, return a new array containing the symmetric difference of them.

    The symmetric difference between two sets is the set of values that appear in either set, but not both.
    Return the values in the order they first appear in the input arrays.
"""


def difference(arr1, arr2):
    difference = []
    for i in arr1:
        if i not in arr2:
            difference.append(i)
    for i in arr2:
        if i not in arr1:
            difference.append(i)
    print(difference)
            
    
difference([1, "a", 2], [2, "b", "a"])