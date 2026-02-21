import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    # Write your code here
    res=""
    bill.remove(bill[k])
    if sum(bill)/2 == b:
        res+=("Bon Appetit")
    else:
        res+=(str(b-(sum(bill)//2)))
        res=int(res)
    return res
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
