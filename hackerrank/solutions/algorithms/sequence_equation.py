import math
import os
import random
import re
import sys

def permutationEquation(p):
    # Write your code here
    res=[]
    p.insert(0," ")
    for i in range(1,len(p)):
        res.append(p.index(p.index(i)))
    return res

permutationEquation([2,3,1])