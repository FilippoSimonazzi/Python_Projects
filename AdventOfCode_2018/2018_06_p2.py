from utils import get_ints, read_file, timer
from collections import defaultdict

@timer
def solve():
    input  = read_file("06")
    points = [tuple(get_ints(line)) for line in input]

    N = 10000
    distances = defaultdict(int)

    x_coords, y_coords = zip(*points)
    top, left, bottom, right = min(y_coords), min(x_coords), max(y_coords), max(x_coords)

    for x in range(left, right + 1):
        for y in range(top, bottom + 1):
            for point in points:
                distances[(x, y)] += abs(x - point[0]) + abs(y - point[1])
    
    result = 0
    for value in distances.values():
        if value < N:
            result += 1
    
    return result

result = solve()
print(f'Solution: {result}')