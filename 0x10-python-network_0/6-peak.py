#!/usr/bin/python3
"""inds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """inds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    arr, leng = list_of_integers, len(list_of_integers)
    half = leng // 2
    if (half == leng - 1 or arr[half] >= arr[half + 1]):
        if (half == 0 or arr[half] >= arr[half - 1]):
            return arr[half]
    if half != leng - 1 and arr[half + 1] > arr[half]:
        return find_peak(arr[half + 1:])
    return find_peak(arr[:half])
