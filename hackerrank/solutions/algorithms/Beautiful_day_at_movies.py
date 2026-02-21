import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    # Write your code here
    beautiful_days = 0
    for i in range(i,j+1):
        reverse = str(i)[::-1]
        if (abs(i-int(reverse))%k) == 0:
            beautiful_days += 1
    return beautiful_days