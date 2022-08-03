from utils import get_ints, read_file, timer

def draw(points):
    gapX  = min(list(zip(*points))[0])
    gapY  = min(list(zip(*points))[1])
    sizeX = max(list(zip(*points))[0]) - gapX + 1
    sizeY = max(list(zip(*points))[1]) - gapY + 1
 
    field = [[" " for y in range(sizeX)] for x in range(sizeY)]

    for point in points:
        field[point[1]-gapY][point[0]-gapX] = "*"
 
    for y in range(sizeY):
        print(''.join(field[y]))

@timer
def solve():
    points = [get_ints(line) for line in read_file("10")]

    found, size = 0, 200

    while found < len(points):
        found = 0
        for point in points:
            point[0] += point[2]
            point[1] += point[3]
            if point[0] >= 0 and \
               point[0] < size and \
               point[1] >= 0 and \
               point[1] < size:
                found += 1
    
    return points

result = solve() 
draw(result)