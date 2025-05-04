"""c2_8.py liner_search"""

import random

def linear_search(arr, key):
    """Linear search function"""
    arr_length = len(arr)
    for i in range(arr_length):
        if arr[i] == key:
            return i
    return None

random.seed(1)
N = 7
B = 50
M = 2
rnbs = random.sample(range(B, B + N), N)
print('org:', rnbs)

for i in range(B - M, B + N + M):
    R = linear_search(rnbs, i)
    print(f'{i}: {R}')