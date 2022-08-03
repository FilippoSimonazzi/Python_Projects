from utils import read_file, timer
from itertools import count

def up_by_1(octo):
    for key in octo.keys():
        octo[key] += 1
    return octo


def flash(pos, octo, flashed):
    x, y = pos
    if pos in flashed:
        return octo, flashed
    flashed.add(pos)
    neighbours = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]
    for n in neighbours:
        pos = (n[0] + x, n[1] + y)
        if pos in octo.keys():
            octo[pos] += 1
            if octo[pos] > 9:
                octo, flashed = flash(pos, octo, flashed)
    return octo, flashed


def reset_flash(octo, flashed):
    for pos in flashed:
        octo[pos] = 0
    return octo


def step(octo):
    to_flash, flashed = [], set()
    octo = up_by_1(octo)
    for key, value in octo.items():
        if value > 9:
            to_flash.append(key)
    for pos in to_flash:
        octo, flashed = flash(pos, octo, flashed)
    
    if len(flashed) == 100:
        return False

    octo = reset_flash(octo, flashed)
    return octo

@timer
def solve():
    input = read_file("11")
    octo = {(x, y): int(e) for x, l in enumerate(input) for y, e in enumerate(l)}
    for it in count(1):
        octo = step(octo)
        if not octo:
            return it

    
result = solve()
print(f'Solution: {result}')