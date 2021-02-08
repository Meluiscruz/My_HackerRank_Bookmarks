#!/bin/python3

import os
import sys

def handshake(n):
    array = []
    if n == 0:
        return 0
    else:
        for _ in range(1,n):
            array.append(_)
        return sum(array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()