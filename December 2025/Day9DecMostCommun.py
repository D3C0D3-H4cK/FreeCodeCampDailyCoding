"""
Most Frequent

Given an array of elements, return the element that appears most frequently.

    There will always be a single most frequent element.
"""

def most_frequent(arr):

    print(max(set(arr), key = arr.count))
most_frequent(["a", "b", "a", "c"])