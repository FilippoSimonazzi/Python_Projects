
from utils import get_ints, read_file, timer
from collections import defaultdict

def get_closest_point(position, points):
    distances = [abs(point[0]-position[0]) + abs(point[1]-position[1]) for point in points]
    min_distance = min(distances)
    
    if distances.count(min_distance) == 1:
        return points[distances.index(min_distance)]
    else:
        return None

@timer
def solve():
    input  = read_file("06")
    points = [tuple(get_ints(line)) for line in input]
    sizes  = defaultdict(int)
    blacklist = set()
    
    x_coords, y_coords = zip(*points)
    top, left, bottom, right = min(y_coords), min(x_coords), max(y_coords), max(x_coords)

    for x in range(left, right+1):
        for y in range(top, bottom+1):
            closest_point = get_closest_point((x, y), points)
            sizes[closest_point] += 1
            if x == left or x == right or y == top or y == bottom:
                blacklist.add(closest_point)

    return max(size for point, size in sizes.items() if point and point not in blacklist)
    
result = solve() 
print(f"Solution: {result}")