import math
import os
import random
import re
import sys

def equalizeArray(arr):
    # Write your code here
    res = 0
    s_array = set(arr)
    counter = list(map(lambda x: arr.count(x), s_array))
    res += (len(arr)-max(counter))
    return res

equalizeArray([3,3,2,1,3])