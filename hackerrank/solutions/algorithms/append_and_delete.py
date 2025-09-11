import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    # Write your code here
    app = 0
    delt = 0
    res = ""
    if len(s) >= len(t):
        delt += (len(s) - len(t))
        for i in range(len(t)):
            if t[i] != s[i]:
                delt += (len(s[i:len(t)]))
                app += (len(t[i:]))
                break
    else:
        app += (len(t) - len(s))
        for i in range(len(s)):
            if t[i] != s[i]:
                delt += (len(s[i:]))
                app += (len(t[i:len(s)]))
                break
    if (app+delt) <= k and delt != 0:
        res += "Yes"
    elif delt == 0 and app < k:
        res += "No"
    else:
        res += "No"
    return res
appendAndDelete("aaaaaaaaaa","aaaaa",7)