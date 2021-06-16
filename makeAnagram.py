#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    tot = 0
    a1 = set(a)
    b1 = set(b)
    c = a1 & b1
    ac = Counter(a)
    bc = Counter(b)
    for c1 in c:
        m = min(ac[c1], bc[c1])
        tot += m
    tot = len(a)-tot+len(b)-tot
    return (tot)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
