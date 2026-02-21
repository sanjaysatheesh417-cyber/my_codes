import math
import os
import random
import re
import sys

def repeatedString(s, n):
    # Write your code here
    res = 0
    res += (s.count("a"))*(n//len(s))
    if n%len(s) > 0:
        l = s[:(n%len(s))]
        res += l.count("a")
    return res

repeatedString("aba",10)