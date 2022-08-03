from utils import read_file, timer
from collections import Counter

@timer
def solve():
    input = read_file("11").split(',')

    pos = [0, 0] # west, nord
    for move in input:
        if move == 'n':
            pos[1] += 1
        elif move == 's':
            pos[1] -= 1
        elif move == 'nw':
            pos[0] += 0.5
            pos[1] += 0.5
        elif move == 'ne':
            pos[0] -= 0.5
            pos[1] += 0.5
        elif move == 'sw':
            pos[0] += 0.5
            pos[1] -= 0.5
        elif move == 'se':
            pos[0] -= 0.5
            pos[1] -= 0.5
    
    return int(abs(pos[0]) + abs(pos[1]))  

result = solve()
print(f'Solution: {result}')