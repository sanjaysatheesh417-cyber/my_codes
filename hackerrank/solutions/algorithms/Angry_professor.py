import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    # Write your code here
    res=""
    n=0
    for i in a:
        if i<=0:
            n+=1
    if n>=k:
        res+="NO"
    else:
        res+="YES"
    return res