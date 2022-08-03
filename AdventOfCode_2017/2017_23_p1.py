from utils import read_file, timer
from itertools import count

def rotate(current, go_right):
    pos = ['up', 'right', 'down', 'left']
    if go_right:
        return pos[(pos.index(current) + 1) % 4]
    else:
        return pos[(pos.index(current) - 1) % 4]

@timer
def solve():
    input = read_file("23")
    
    grid = {}

    for x, row in enumerate(input):
        for y, col in enumerate(row):
            grid[(x, y)] = 1 if input[x][y] == '#' else 0

    virus_pos = (len(input) // 2, len(input[0]) // 2)
    dir = 'up'

    tot_infected = 0
    N = 10000

    for it in range(N):
        # change directions
        if virus_pos not in grid.keys():
            grid[virus_pos] = 0

        #print(f'\n ---- {it = } ----')
        #print(f'{virus_pos = }, Infected: {grid[virus_pos]}, Direction: {dir}\n')

        dir = rotate(dir, grid[virus_pos]) # rotate right if infected

        # change nodes
        grid[virus_pos] = abs(grid[virus_pos] - 1) # always flip between 0 and 1
        if grid[virus_pos]:
            tot_infected += 1

        #print(f'{virus_pos = }, Infected: {grid[virus_pos]}, Direction: {dir}\n')

        # move forward in direction
        x, y = virus_pos
        if dir == 'up':
            x -= 1
        elif dir == 'down':
            x += 1
        elif dir == 'right':
            y += 1
        elif dir == 'left':
            y -= 1
        virus_pos = (x, y)

    return tot_infected
    
result = solve()
print(f'Solution: {result}')