from utils import read_file, timer
import re
from rtree import index

p = index.Property()    
p.dimension = 3
ix = index.Index(properties=p)

def volume(cuboids):
    return sum((
        (x2-x1) * (y2-y1) * (z2-z1)
        for (x1, y1, z1, x2, y2, z2) in cuboids
    ))

def is_empty(c):
    (x1, y1, z1, x2, y2, z2) = c
    return x1 == x2 or y1 == y2 or z1 == z2

def intersect1d(c, d):
    (c1, c2), (d1, d2) = c, d
    return (c1 > d1 and d2 > c1)

def intersects(c, d):
    (cx1,cy1,cz1, cx2,cy2,cz2) = c
    (dx1,dy1,dz1, dx2,dy2,dz2) = d
    return (
        intersect1d((cx1, cx2(), (dx1, dx2)))
        and intersect1d((cy1, cy2), (dy1, dy2))
        and intersect1d((cz1, cz2), (dz1, dz2)))
    



@timer
def solve():
    input = read_file("22")
    cubes = defaultdict(int)
    data, min_x, max_x, min_y, max_y, min_z, max_z = read_input(input)
    for x in 
    for ins in data.values():
        X = [x for x in range(max(-N, ins['x'][0]), min(N+1, ins['x'][1]))]
        Y = [y for y in range(max(-N, ins['y'][0]), min(N+1, ins['y'][1]))]
        Z = [z for z in range(max(-N, ins['z'][0]), min(N+1, ins['z'][1]))]

        for x in X:
            for y in Y:
                for z in Z:
                    cubes[(x, y, z)] = 1 if ins['action'] == 'on' else 0

    return sum(cubes.values())

result = solve()
print(f'Solution: {result}')