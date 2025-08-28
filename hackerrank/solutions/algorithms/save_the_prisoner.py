import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    # Write your code here
    res = 0
    if (s+m)-1 > n:
        p = ((s+m)-2)-n
        res += (p%n)+1
    else:
        res += (s+m-1)
    return res

saveThePrisoner(3,7,3)