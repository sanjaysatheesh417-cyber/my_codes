import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    n=100
    a = []
    for i in c:
        a.append(i)
        if len(a)%k == 0 and len(a) >= len(c):
            a.append(c[0])
            break
    for j in range(0,len(a),k):
        if a[j] == 0:
            n-=1
        else:
            n-=3
    return n

jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0],2)