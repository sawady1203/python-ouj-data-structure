"""c2_9.py binary_search"""

import random

def binary_search(arr, value):
    """Binary search function"""
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = low + (high - low) // 2
        # print(f'low: {low}, mid: {mid}, high: {high}')
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return None

random.seed(1)
N = 7
B = 50
M = 2
rnbs = random.sample(range(B, B + N), N)
rnbs.sort()
print('asc:', rnbs)

for i in range(B - M, B + N + M):
    R = binary_search(rnbs, i)
    print(f'{i}: {R}')