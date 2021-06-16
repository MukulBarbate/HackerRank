#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    l = []
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            l.append("".join(sorted(s[j:j+i])))
    l.sort()
    count = 0
    print(l)
    for x in range(len(l)):
        if  l[x+1:].count(l[x]):
            count+=(l[x+1:].count(l[x]))
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
