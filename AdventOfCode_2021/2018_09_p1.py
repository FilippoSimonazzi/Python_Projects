from utils import read_file, timer


def around(x, y, N, M, grid):
    out = []
    if x > 0:
        out.append(grid[x - 1][y])
    if x < N-1:
        out.append(grid[x + 1][y])
    if y > 0:
        out.append(grid[x][y - 1])
    if y < M-1:
        out.append(grid[x][y + 1])
    return out


def value_point(x, y, N, M, grid):
    p = grid[x][y]
    for point in around(x, y, N, M, grid):
        if p >= point:
            return 0
    return p + 1

@timer
def solve():
    input = read_file("09")
    grid = []
    for row in input:
        grid.append([])
        for ch in row:
            grid[-1].append(int(ch))
    M, N = len(grid[0]), len(grid)
    tot = 0
    for x in range(N):
        for y in range(M):
            tot += value_point(x, y, N, M, grid)
    return tot

result = solve()
print(f'Solution: {result}')