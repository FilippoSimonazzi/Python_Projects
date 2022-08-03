from utils import read_file, timer
from collections import defaultdict
import sys
import collections

sys.setrecursionlimit(5000)

settled, flowing = set(), set()

def fill(pt, clay, y_min, y_max, direction=(0, 1)):
    flowing.add(pt)
    below = (pt[0], pt[1] + 1)
    
    if not clay[below] and below not in flowing and 1 <= below[1] <= y_max:
        fill(below, clay, y_min, y_max)

    if not clay[below] and below not in settled:
        return False

    left, right = (pt[0] - 1, pt[1]), (pt[0] + 1, pt[1])
    left_filled = clay[left] or left not in flowing and fill(left, clay, y_min, y_max, direction=(-1, 0))
    right_filled = clay[right] or right not in flowing and fill(right, clay, y_min, y_max, direction=(1, 0))

    if direction == (0, 1) and left_filled and right_filled:
        settled.add(pt)

        while left in flowing:
            settled.add(left)
            left = (left[0] - 1, left[1])

        while right in flowing:
            settled.add(right)
            right = (right[0] + 1, right[1])

    return direction == (-1, 0) and (left_filled or clay[left]) or \
        direction == (1, 0) and (right_filled or clay[right])

@timer
def solve():
    clay = collections.defaultdict(bool)
    input = read_file('17')
    for line in input:
        a, brange = line.split(',')
        if a[0] == 'x':
            x = int(a.split('=')[1])
            y1, y2 = map(int, brange.split('=')[1].split('..'))

            for y in range(y1, y2 + 1):
                clay[(x, y)] = True
        else:
            y = int(a.split('=')[1])
            x1, x2 = map(int, brange.split('=')[1].split('..'))

            for x in range(x1, x2 + 1):
                clay[(x, y)] = True
    
    y_min, y_max = min(clay, key=lambda p: p[1])[1], max(clay, key=lambda p: p[1])[1]
    fill((500, 0), clay, y_min, y_max)
    
    print(f'part 1: {len([pt for pt in flowing | settled if y_min <= pt[1] <= y_max])}')
    print(f'part 1: {len([pt for pt in settled if y_min <= pt[1] <= y_max])}')


    pass

result = solve()
print(f'Solution: {result}')