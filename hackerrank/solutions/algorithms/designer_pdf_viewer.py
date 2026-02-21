import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    # Write your code here
    res=0
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    c_height=[]
    for i in alphabets:
        if i in word:
            c_height.append(h[alphabets.index(i)])
    res+=(max(c_height)*len(word))
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
