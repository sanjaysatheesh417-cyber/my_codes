import math
import os
import random
import re
import sys

def acmTeam(topic):
    # Write your code here
    counts = []
    pairs = []
    for i in range(len(topic)):
        for j in range(len(topic)):
            if {i,j} not in pairs:
                pairs.append({i,j})
    pairs1 = map(list(lambda x: list(x),pairs))
    for m in pairs1:
        count = 0
        for l in range(len(topic[0])):
            if topic[m[0]][l]==0 and topic[m[1]][l]==0:
                count += 0
            else:
                count += 1
        counts.append(count)
    return pairs
acmTeam(["10101","11100","11010","00101"])