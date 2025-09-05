import math
import os
import random
import re
import sys

from hackerrank.testcases.test_algorithm.test_picking_numbers import test_pickingNumbers


def jumpingOnClouds(c, k):
    n=100
    temp = 0
    a=[]
    for i in range(len(c)):
        if (temp+k) >= len(c):
            temp -= len(c)
        temp1 = (temp + k) % n
        if (temp1+k) == len(c):
            a.append(c[temp1])
            if k != len(c):
                a.append(c[0])
            break
        else:
            a.append(c[temp1])
            temp += k
            continue
    for j in range(len(a)):
        if a[j] == 0:
            n -= 1
        else:
            n -= 3
    return n

jumpingOnClouds([1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1],19)