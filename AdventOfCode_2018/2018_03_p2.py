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
    used_spots = set()
    for i in range(top, top+height):
        for j in range(left, left+width):
            grid[i][j] += 1
            used_spots.add((i, j))
    return grid, used_spots


def compute_result(SPOTS):
    keys = list(SPOTS.keys())
    for i in range(len(keys)):
        check = True
        for j in range(len(keys)):
            if i != j:
                if not SPOTS[keys[i]].isdisjoint(SPOTS[keys[j]]):
                    check = False
                    break
        if check:
            return keys[i]


@timer
def solve():
    input = read_file('03')
    N = 1000
    grid = create_grid(N)
    SPOTS = {}
    for claim in input:
        ID, left, top, width, height = read_input(claim)
        grid, used_spots = update_grid(grid, left, top, width, height)
        SPOTS[ID] = used_spots
    return compute_result(SPOTS)

result = solve()
print(f'Solution: {result}')