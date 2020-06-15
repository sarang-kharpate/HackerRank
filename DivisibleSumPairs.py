import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    pairs = []
    for i in range(0, n-1):
        count = i+1
        while (count < n):
            if ((ar[i] + ar[count]) % k == 0):
                pairs.append(1)
            count+=1
    return len(pairs)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input('Array Length and Divisor: ').split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input('Array: ').rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(f'Number of pairs are : {result}')

    #fptr.write(str(result) + '\n')

    #fptr.close()
