#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter #cornerstone

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    Dict_of_socks = Counter(ar) #This is the cornerstone of this crap
    Acum = 0
    for key in Dict_of_socks:
        if Dict_of_socks[key] == 1:
            pass
        elif Dict_of_socks[key]%2 == 0:
            Acum += (Dict_of_socks[key]/2)
        else:
            Acum += (Dict_of_socks[key]//2)
    
    return int(Acum)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()