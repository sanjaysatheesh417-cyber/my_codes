import math
import os
import random
import re
import sys

def findDigits(n):
    # Write your code here
    a = str(n)
    res=0
    for i in a:
        if int(i) != 0:
            if n%int(i)==0 :
                res+=1
    return res

findDigits(124)