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
        for j in range( i+1,len(topic)):
            pairs.append((topic[i], topic[j]))
    for pair in pairs:
        count = 0
        for l in range(len(pair[0])):
            if (pair[0][l] == "1") or (pair[1][l] == "1"):
                count += 1
        counts.append(count)
    return (max(counts),counts.count(max(counts)))
acmTeam(["10101","11110","00010"])