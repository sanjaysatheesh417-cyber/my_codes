import math
import os
import random
import re
import sys

def viralAdvertising(n):
    # Write your code here
    likes=0
    shared = 5
    for i in range(1,n+1):
        likes += shared//2
        shared = ((shared//2)*3)
    return likes

viralAdvertising(3)