import numpy as np
from utils import read_file, timer

@timer
def solve():
    input = read_file("14")
    n = 128
    used = 0
    disk = np.zeros((n, n))

    #for row in range(n):
    #    key = input + '-' + str(row)

    input = 'flqrgnkx'

    out = hex(ord('a'))[2:]
    if len(out) == 1:
        out = int('0' + out)
    else:
        out = int(out)
    out = bin(out)
    




    return out

result = solve()
print(f'Solution: {result}')