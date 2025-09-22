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
            if i != j:
                if {i,j} not in pairs:
                    pairs.append({i,j})
    pairs = list(map(lambda x: list(x), pairs))
    for p in pairs:
        sub_known = []
        counter = 0
        for k in range(len(topic[0])):
            sub_known.append([topic[p[0]][k], topic[p[1]][k]])
        for l in sub_known:
            if l == ["1", "0"] or l == ["0", "1"] or l == ["1", "1"]:
                counter += 1
        counts.append(counter)
    res = [max(counts),counts.count(max(counts))]
    return res

acmTeam(["10101","11100","11010","00101"])