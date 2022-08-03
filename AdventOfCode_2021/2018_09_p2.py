from utils import read_file, timer
from math import prod

input = read_file("09")

# create grid
grid = {(y, x): int(h) for y, l in enumerate(input)
                       for x, h in enumerate(l.strip())}


def neighbours(x, y):
    return filter(lambda n: n in grid, 
        [(x, y-1), (x, y+1), (x-1, y), (x+1, y)])

def is_low(point):
    return all(grid[point] < grid[n] for n in neighbours(*point))

# get low points
low_points = list(filter(is_low, grid))
sol_1 = sum(grid[p]+1 for p in low_points)

print(f'\nSolution part 1: {sol_1}\n')

def count_basin(p):
    if grid[p] == 9:  # 9 is never in basin, stop counting.
        return 0
    del grid[p] # avoid further visits
    return 1 + sum(map(count_basin, neighbours(*p)))

basins = [count_basin(p) for p in low_points]
sol_2 = prod(sorted(basins)[-3:])
print(f'\nSolution part 2: {sol_2}\n')
