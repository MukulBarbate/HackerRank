#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    top = []
    mid = []
    bot = []
    for x in range(len(arr)-2):
        n = arr[x]
        m = arr[x+2]
        o = arr[x+1]
        for y in range(len(arr)-2):
            top.append(sum(n[y:y+3]))
            mid.append(o[y+1])
            bot.append(sum(m[y:y+3]))
            
    res = [top[e]+mid[e]+bot[e] for e in range(len(top))]
     
    print(top,mid,bot,res, sep="\n")
    return max(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
