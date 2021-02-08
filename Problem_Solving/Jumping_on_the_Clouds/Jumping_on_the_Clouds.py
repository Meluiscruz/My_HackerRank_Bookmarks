#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    split_list = [list(j) for i, j in groupby(c)]
    jumps = 0
    
    for index in range(len(split_list)):
        if len(split_list[index]) % 2 == 0 and split_list[index][0] == 0:
            jumps += len(split_list[index]) // 2
        elif len(split_list[index]) % 2 == 1 and split_list[index][0] == 0:
            jumps += (len(split_list[index]) // 2) + (len(split_list[index]) % 2) -1
        elif split_list[index][0] == 1:
            jumps +=1

    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()