from collections import defaultdict
from utils import read_file, timer
from itertools import count
import math


def create_possible_y(n, minY, maxY):
    a = 1/n * (minY - n/2 + n**2/2)
    b = 1/n * (maxY - n/2 + n**2/2)
    return list(range(math.ceil(a), math.floor(b)+1))


@timer
def solve():
    input = read_file("17")
    areaX, areaY = input.split(' ')[2], input.split(' ')[3]
    minX, maxX = [int(areaX.split('..')[0][2:]), int(areaX.split('..')[1][:-1])]
    minY, maxY = [int(areaY.split('..')[0][2:]), int(areaY.split('..')[1])]
    
    highestY = 0
    for n in range(1, 1000):
        possible_y = create_possible_y(n, minY, maxY)
        for y in possible_y:
            if y > highestY:
                highestY = y
    return int(highestY * (highestY + 1) / 2)
    

result = solve()
print(f'Solution: {result}')