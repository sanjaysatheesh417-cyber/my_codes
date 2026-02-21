import math
import os
import random
import re
import sys

def squares(a, b):
    # Write your code here
    result = 0
    n = 0
    for i in range(1,b):
        if n >= b:
            break
        if i % 2 != 0:
            n += i
            if n in range(a,b+1):
                result += 1
    return result

squares(17,24)