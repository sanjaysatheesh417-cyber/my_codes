import math
import os
import random
import re
import sys

def circularArrayRotation(a, k, queries):
    # Write your code here
    res=[]
    for i in range(k):
        a.insert(0,a[len(a)-1])
        a.pop()
    for j in queries:
        res.append(a[j])
    return res

circularArrayRotation([3,4,5],2,[1,2])