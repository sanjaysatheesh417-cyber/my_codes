import math
import os
import random
import re
import sys

def taumBday(b, w, bc, wc, z):
    # Write your code here
    min_cost = 0
    if b*bc > (wc+z)*b:
        if w*wc > (bc+z)*w:
            min_cost += (wc+z)*b
            min_cost += (bc+z)*w
        else:
            min_cost += (wc+z)*b
            min_cost += w*wc
    else:
        if w * wc < (bc + z) * w:
            min_cost += w*wc
            min_cost += b*bc
        else:
            min_cost += (bc + z) * w
            min_cost += b*bc
    return min_cost
taumBday(3,6,9,1,1)