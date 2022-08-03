from utils import read_file, timer
import numpy as np

def read_input(x):
    splits = x.split(' ')
    ID = splits[0][1:]
    left = splits[2].split(',')[0]
    top = splits[2].split(',')[1][:-1]
    width = splits[3].split('x')[0]
    height = splits[3].split('x')[1]
    return ID, int(left), int(top), int(width), int(height)


def create_grid(N):
    grid = np.zeros((N, N))
    return grid

def update_grid(grid, left, top, width, height):
    N = len(grid[0])
    for i in range(top, top+height):
        for j in range(left, left+width):
            grid[i][j] += 1
    return grid


def compute_result(grid, N):
    result = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 1:
                result += 1
    return result

@timer
def solve():
    input = read_file('03')
    N = 1000
    grid = create_grid(N)
    for claim in input:
        ID, left, top, width, height = read_input(claim)
        grid = update_grid(grid, left, top, width, height)
    return compute_result(grid, N)

result = solve()
print(f'Solution: {result}')