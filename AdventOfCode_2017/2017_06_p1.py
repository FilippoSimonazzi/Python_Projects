import re
from utils import read_file, timer
import numpy as np

@timer
def solve():
    input = read_file("06").split()
    input = list(map(int, input))

    n_it = 0
    seen = set()
    seen.add(tuple(input))
    while True:
        n_it += 1
        start_idx = np.argmax(input)
        value = input[start_idx]
        for i in range(value):
            input[(start_idx + 1 + i) % len(input)] += 1
            input[start_idx] -= 1
    
        if tuple(input) in seen:
            break
        else:
            seen.add(tuple(input))
        
    return n_it


result = solve()
print(f'Solution: {result}')