import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    # Write your code here
    result = [len(arr)]
    arr2 = arr
    while len(arr2) != 0:
        arr1 = []
        for j in arr2:
            j -= min(arr2)
            if j > 0:
                arr1.append(j)
        arr2 = arr1
        result.append(len(arr1))

    return result[:len(result)-1]

cutTheSticks([5,4,4,2,2,8])