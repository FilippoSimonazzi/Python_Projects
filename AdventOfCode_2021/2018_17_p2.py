from collections import defaultdict
from utils import read_file, timer
from itertools import count
import math


def create_possible_y(n, minY, maxY):
    a = 1/n * (minY - n/2 + n**2/2)
    b = 1/n * (maxY - n/2 + n**2/2)
    return list(range(math.ceil(a), math.floor(b)+1))

def compute_y(n, y):
    y = n*y - (n**2)/2 + n/2
    if y < 0:
        return math.ceil(y)
    return math.floor(y)

def compute_x(n, x, verbose=False):
    if verbose:
        print(n, x, x <= n)
        print()
    if x >= n:
        x = n*x - (n**2)/2 + n/2
    else:
        x = (x**2)/2 + x/2
    if x < 0:
        return math.ceil(x)
    return math.floor(x)

@timer
def solve():
    input = read_file("17")
    areaX, areaY = input.split(' ')[2], input.split(' ')[3]
    minX, maxX = [int(areaX.split('..')[0][2:]), int(areaX.split('..')[1][:-1])]
    minY, maxY = [int(areaY.split('..')[0][2:]), int(areaY.split('..')[1])]
    
    values = set()
    possible_y = set()
    for n in range(1, 1000):
        possible_y = create_possible_y(n, minY, maxY)
        for y in possible_y:
            for temp_n in range(1, n+1):
                for x in range(maxX + 1):
                    temp_y = compute_y(temp_n, y)
                    temp_x = compute_x(temp_n, x)
                    if minY <= temp_y <= maxY and minX <= temp_x <= maxX:
                        values.add((x, y))
    return len(values)
    

result = solve()
print(f'Solution: {result}')