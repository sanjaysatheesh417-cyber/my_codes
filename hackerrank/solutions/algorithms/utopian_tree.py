import math
import os
import random
import re
import sys

def utopianTree(n):
    # Write your code here
    res=1
    for i in range(1,n+1):
        if i%2 != 0:
            res+=res
        else:
            res+=1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
