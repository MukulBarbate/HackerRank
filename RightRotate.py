#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotRight(a, d):
    # Write your code here
    for x in range (d):
        e = -1
        a2 = a.copy()
        for y in range(len(a)):
          a2[y] = a[e]
          e = (e+1)%len(a)
        a = a2
    return a

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotRight(a, d)

    print(result)
