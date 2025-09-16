import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    # Write your code here
    result = [len(arr)]
    arr1 = arr
    for i in range(max(arr)-min(arr)+1):
        a = []
        arr1 = list(map(lambda x:x-(min(arr)),arr1))
        for j in arr1:
            if j != 0:
                a.append(j)
        result.append(len(a))

    return result

cutTheSticks([5,4,4,2,2,8])