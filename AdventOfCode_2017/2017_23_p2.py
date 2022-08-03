from utils import read_file, timer
from itertools import count

def rotate(current, status):
    pos = ['up', 'right', 'down', 'left']
    if status == 'infected':
        return pos[(pos.index(current) + 1) % 4]
    elif status == 'clean':
        return pos[(pos.index(current) - 1) % 4]
    elif status == 'flagged':
        return pos[(pos.index(current) + 2) % 4]
    elif status == 'weakened':
        return current

def update_status(current):
    if current == 'clean':
        return 'weakened'
    elif current == 'weakened':
        return 'infected'
    elif current == 'infected':
        return 'flagged'
    elif current == 'flagged':
        return 'clean'


@timer
def solve():
    input = read_file("23")

    #input = ['..#', '#..', '...']
    grid = {}

    for x, row in enumerate(input):
        for y, col in enumerate(row):
            grid[(x, y)] = 'infected' if input[x][y] == '#' else 'clean'

    virus_pos = (len(input) // 2, len(input[0]) // 2)
    dir = 'up'

    tot_infected = 0
    N = 10000000

    for it in range(N):
        if it % 10 ** 5 == 0:
            print(it)
        # change directions
        if virus_pos not in grid.keys():
            grid[virus_pos] = 'clean'

        #print(f'\n ---- {it = } ----')
        #print(f'{virus_pos = }, Infected: {grid[virus_pos]}, Direction: {dir}\n')

        dir = rotate(dir, grid[virus_pos]) # rotate right if infected

        # change nodes
        grid[virus_pos] = update_status(grid[virus_pos]) 
        if grid[virus_pos] == 'infected':
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