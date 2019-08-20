#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    K = [[0 for j in range(n+1)] for i in range(len(c)+1)]
    return getWays2(n, c, K)
    
def getWays2(n, c, K):
    for i in range(len(c)+1):
        for j in range(n+1):
            if (j==0):
                K[i][j] = 1
            elif i==0:
                K[i][j] = 0
            else:
                w = c[i-1]
                if j < w:
                    K[i][j] = K[i-1][j]
                elif j == w:
                    K[i][j] = K[i-1][j] + 1
                else:
                    K[i][j] = K[i-1][j] + K[i][j-w] 
    return K[len(c)][n]


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the         # values given by 'c'

    ways = getWays(n, c)

    print(ways)
