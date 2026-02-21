import math
import os
import random
import re
import sys


def pageCount(n, p):
    # Write your code here
    pages=[[1]]
    res=[0,0]
    for i in range(2,n,2):
        pages.append([i,i+1])
    if n%2 == 0:
        pages.append([n])
    for j in pages:
        res[0]+=1
        if p in j:
            res[0]-=1
            break
    pages.reverse()
    for k in pages:
        res[1]+=1
        if p in k:
            res[1]-=1
            break
    return min(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
