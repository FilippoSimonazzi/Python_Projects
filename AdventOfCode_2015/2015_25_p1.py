from turtle import st
from utils import read_file, timer

def build_grid(n, start=1):
    """
    it builds the grid up to row n and column n
    """
    num = start
    grid = dict()
    grid[(1, 1)] = num
    for i in range(1, n+1):
        for j in range(1, i):
            num += 1
            grid[(i, j)] = num
            num += 1
            grid[(j, i)] = num
    return grid

@timer
def solve():
    input = read_file("25")
    
    grid = build_grid(n=4)
    print(grid)

result = solve()
print(f'Solution: ')