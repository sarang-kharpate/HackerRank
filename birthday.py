#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    num_of_ways = []
    for i in range(0, len(s)):
        j = i

        li = []
        for j in range(j, j+m):
            li.append(s[j])
        if sum(li) == d:
            num_of_ways.append(1)
        if i + m == len(s):
            break
    if len(num_of_ways) > 0:
        return len(num_of_ways)
    else:
        return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input('Lenght of array:').strip())

    s = list(map(int, input('Actuall Array:').rstrip().split()))

    dm = input('Date and Month:').rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
