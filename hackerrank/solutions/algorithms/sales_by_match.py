import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    # Write your code here
    ar1=set(ar)
    count=[]
    pairs=0
    for i in ar1:
        count.append(ar.count(i))
    for j in count:
        if j%2==0 or (j%2!=0 and j>2):
            pairs+=(j//2)
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
