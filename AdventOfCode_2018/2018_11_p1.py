from collections import defaultdict
import re
from utils import read_file, timer, get_ints


def compute_pow_level(x, y, input):
    rack_id = x + 10
    pow_level = rack_id * y
    pow_level += input
    pow_level *= rack_id
    if len(str(pow_level)) >= 3:
        pow_level = int(str(pow_level)[-3])
    else:
        pow_level = 0
    pow_level -= 5
    return pow_level


@timer
def solve():
    input = get_ints(read_file("11"))[0]
    N = 300
    grids = defaultdict(int)
    for i in range(1, N-1):
        for j in range(1, N-1):
            for x in range(i, i+3):
                for y in range(j, j+3):
                    grids[(i, j)] += compute_pow_level(x, y, input)

    max_value = 0
    for key, value in grids.items():
        if value > max_value:
            max_value = value
            result = key
    return result

result = solve()
print(f'Solution: {result}')