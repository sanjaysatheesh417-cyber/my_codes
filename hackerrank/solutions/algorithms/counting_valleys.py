import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    res = 0
    counter = 0
    old_counter = 0
    for i in range(steps):
        old_counter = counter
        if path[i] == 'U':
            counter+=1
        else:
            counter-=1
        if counter == 0 and old_counter == -1 and i!=0:
            res+=1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
