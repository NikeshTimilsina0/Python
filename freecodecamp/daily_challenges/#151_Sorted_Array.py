"""Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

In ascending order (lowest to highest), return "Ascending".
In descending order (highest to lowest), return "Descending".
Not sorted in ascending or descending order, return "Not sorted"."""
def is_sorted(arr):

    ascending=sorted(arr)
    descending=ascending[::-1]
    if ascending==arr:
        return "Ascending"
    elif descending==arr:
        return "Descending"
    else:
        return "Not sorted"
print(is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]))
print(is_sorted([3.14, 2.71, 1.61, 0.57]))
print(is_sorted([0.4, 0.5, 0.3]))