import math
import os
import random
import re
import sys

def birthday(s, d, m):
    # Write your code here
    res=0
    for i in range(len(s)):
        if sum(s[i:i+m])==d:
            res+=1
    return res

birthday([2,2,1,3,2],4,2)