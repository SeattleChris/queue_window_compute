#!/bin/python3

import os
from collections import deque

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    """Solve the problem using a sliding window maximum approach."""
    mins = []
    for width in queries:
        window_i = deque()
        maxs = []
        for idx, val in enumerate(arr):
            if window_i and window_i[0] < idx - width + 1:
                window_i.popleft()  # Position no longer in window
            while window_i and arr[window_i[-1]] < val:
                window_i.pop()  # current val is max for following vals
            window_i.append(idx)
            if idx >= width - 1:  # val at leftmost index is max
                maxs.append(arr[window_i[0]])
        mins.append(min(maxs))
    return mins


def brute_solve(arr, queries):
    """This is too slow of a solution."""
    size = len(arr)
    return [
        min(max(arr[i:i + width]) for i in range(size - width + 1))
        for width in queries
    ]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = solve(arr, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
