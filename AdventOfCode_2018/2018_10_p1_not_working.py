import re
from utils import get_ints, read_file, timer

def read_line(line):
    line = line[10:]
    p_x, p_y = int(line.split(', ')[0]), int((line.split(', ')[1].split('>'))[0])

    line = line.split('<')[1]
    v_x, v_y = int(line.split(', ')[0]), int((line.split(', ')[1].split('>'))[0])

    return [p_x, p_y, v_x, v_y]

def update_points(points):
    for point in points:
        point[0] += point[2]
        point[1] += point[3]

    return points

def draw(points):
    print('*******************')
    gapX  = min(list(zip(*points))[0])
    gapY  = min(list(zip(*points))[1])
    sizeX = max(list(zip(*points))[0]) - gapX + 1
    sizeY = max(list(zip(*points))[1]) - gapY + 1

    field = [[" " for y in range(sizeX)] for x in range(sizeY)]

    for point in points:
        field[point[1]-gapY][point[0]-gapX] = "#"
 
    for y in range(sizeY):
        print(''.join(field[y]))

    print('*******************\n\n\n')

@timer
def solve():
    points = [read_line(line) for line in read_file('10')]
    seconds = 0
    N = 10    
    while seconds < N:
        points = update_points(points)
        draw(points)
        seconds += 1        
    
    return points

result = solve()