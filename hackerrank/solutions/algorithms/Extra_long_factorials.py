import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    # Write your code here
    res = 1
    for i in range(n,1,-1):
        res*=i
    return res

extraLongFactorials(25)