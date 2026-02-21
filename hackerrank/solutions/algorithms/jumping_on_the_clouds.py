import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    # Write your code here
    path = []
    n = 0
    for i in range(len(c)):
        if (len(c) - n) > 2:
            if c[n + 1] == 1:
                path.append(n + 2)
                n += 2
            else:
                if c[n + 2] == 0:
                    path.append(n + 2)
                    n += 2
                else:
                    path.append(n + 1)
                    n += 1
        else:
            if ((len(c) - 1) - n) == 1:
                path.append(n + 1)
            elif ((len(c) - 1) - n) == 2:
                path.append(n + 2)
            else:
                break
            break

    return len(path)

jumpingOnClouds([0,0,1,0,0,1,0])