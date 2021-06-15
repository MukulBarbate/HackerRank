#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    l1 = arr.copy()
    l1.sort()
    
    while(arr!= l1):
        for x in range(len(arr)):
            if arr[x] != x+1:
                arr[arr[x]-1],arr[x] = arr[x],arr[arr[x]-1]
                swap += 1

    return swap
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
