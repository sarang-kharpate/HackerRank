import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    count = [0]*6
    for t in arr:
        print(f'Value of t: {t}')
        count[t] += 1

    print(f'count: {count}')
    return count.index(max(count))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
