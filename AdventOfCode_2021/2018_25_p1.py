from utils import read_file, timer
from itertools import count

def move_south(grid):
    N = max(list(grid.keys()), key=lambda item: item[0])[0]
    for key, value in grid.items():
        d, _ = value
        if d == 'v':
            x, y = key
            new_x = 0 if (x+1) > N else x+1
            if grid[(new_x, y)][0] == '.':
                grid[key] = (d, True)
    new_grid = grid.copy()
    for key, value in grid.items():
        d, move = value
        if d == 'v' and move:
            x, y = key
            new_x = 0 if (x+1) > N else x+1
            new_grid[(new_x, y)] = ('v', False)
            new_grid[key] = ('.', False)
    return new_grid


def move_east(grid):
    N = max(list(grid.keys()), key=lambda item: item[1])[1]    
    for key, value in grid.items():
        d, _ = value
        if d == '>':
            x, y = key
            new_y = 0 if (y+1)>N else y+1
            if grid[(x, new_y)][0] == '.':
                grid[key] = (d, True)
    new_grid = grid.copy()
    for key, value in grid.items():
        d, move = value
        if d == '>' and move:
            x, y = key
            new_y = 0 if (y+1)>N else y+1
            new_grid[(x, new_y)] = ('>', False)
            new_grid[key] = ('.', False)
    return new_grid

def move(grid):
    new_grid = move_east(grid)
    new_grid = move_south(new_grid)
    if new_grid == grid:
        return False
    return new_grid

def display(grid):
    N = max(list(grid.keys()), key=lambda item: item[0])[0]
    l = []
    for n in range(N+1):
        l.append([x[0] for k, x in grid.items() if k[0] == n])
    for line in l:
        print(''.join(line))
    print()


@timer
def solve():
    input = read_file("25")
    grid = {(x, y): (v, False) for x, l in enumerate(input) for y, v in enumerate(l)}
    for it in count(1):
        if it % 100 == 0:
            print(it               )
        grid = move(grid)
        if not grid:
            return it
    

result = solve()
print(f'Solution: {result}')