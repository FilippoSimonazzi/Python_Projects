from functools import reduce
from utils import read_file, timer


@timer
def solve():
    input = read_file("13")
    divide = input.index('')
    points, folds = input[:divide], input[divide + 1:]

    points = [tuple(map(int, p.split(','))) for p in points]
    folds = [f.split(' ')[-1].split('=') for f in folds]
    
    # part 1
    folds = folds[:1]

    xfolds = [int(f[1]) for f in folds if f[0] == 'x']
    yfolds = [int(f[1]) for f in folds if f[0] == 'y']
    
    maxX, maxY = max(list(zip(*points))[0]), max(list(zip(*points))[1])
    dimX = min(xfolds) if len(xfolds) > 0 else maxX + 1
    dimY = min(yfolds) if len(yfolds) > 0 else maxY + 1

    grid = [[0 for x in range(dimX)] for y in range(dimY)]

    for p in points:
        x, y = p
        for yaxis in yfolds:
            y = yaxis - abs(y - yaxis)
        for xaxis in xfolds:
            x = xaxis - abs(x - xaxis)
        if x < 0 or y < 0:
            continue
        grid[y][x] = 1
    
    print('\n'.join([''.join(['#' if x else '' for x in row]) for row in grid]))

    return sum(sum(row) for row in grid)

result = solve()
print(f'Solution: {result}')