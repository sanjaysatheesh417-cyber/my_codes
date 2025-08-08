import math
import os
import random
import re
import sys

def pickingNumbers(a):
    # Write your code here
    outcomes=[]
    res=[]
    for i in set(a):
        for j in set(a):
            if abs(j-i) <= 1:
                outcomes.append([i,j])
    for k in outcomes:
        if k[0] == k[1]:
            res.append(a.count(k[0]))
        else:
            res.append((a.count(k[0]))+(a.count(k[1])))
    return max(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
