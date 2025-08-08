import math
import os
import random
import re
import sys


def catAndMouse(x, y, z):
    res=""
    d1=[x,z]
    d2=[y,z]
    d1.sort()
    d2.sort()
    if (d1[1]-d1[0]) < (d2[1]-d2[0]):
        res+="Cat A"
    elif (d1[1]-d1[0]) > (d2[1]-d2[0]):
        res+="Cat B"
    else:
        res+="Mouse C"
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
