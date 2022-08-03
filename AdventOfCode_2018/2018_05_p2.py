from os import remove
from utils import read_file, timer
from collections import deque


def react(polymer):
    polymer = deque(list(polymer) + ['.'])
    while polymer[1] != '.':
        if polymer[0] != polymer[1] and \
            polymer[0].upper() == polymer[1].upper():
            polymer.popleft(), polymer.popleft()
            polymer.rotate()
        else:
            polymer.rotate(-1)
    polymer.rotate(-1)
    polymer.popleft()
    return polymer


def remove_letter(polymer, letter):
    return [unit for unit in polymer if unit != letter.lower() and unit != letter.upper()]


@timer
def solve():
    input = read_file('05')[0]
    polymer = react(input)
    result = len(polymer)
    original = input

    for num in range(97, 123):
        polymer = remove_letter(original, chr(num))
        polymer = react(polymer)
        result = min(result, len(polymer))
    
    return result

    
result = solve()
print(f'Solution: {result}')