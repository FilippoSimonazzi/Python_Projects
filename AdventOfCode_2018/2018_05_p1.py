from utils import read_file, timer
from collections import deque

"""
def reaction(input):
    while True:
        react_idx = []
        for i in range(len(input) - 1):
            if input[i].lower() == input[i + 1].lower():
                react_idx.append(i)
        if react_idx == []:
            return input
        
        i = 0
        remove_idx = True
        while remove_idx:
            if i == len(react_idx):
                remove_idx = False
            if react_idx[i + 1] == react_idx[i] + 1:
                react_idx.pop(i + 1)
                i = 0
            else:
                i += 1
        for idx in react_idx:
            is_lower = input[idx].islower()
            if is_lower:
                if not input[idx + 1].islower():
                    if idx + 2 <= len(input):
                        input = input[:idx] + input[idx + 2:]
                    else:
                        input = input[:idx]
                else:
                    react_idx.remove(idx)
            else:
                if input[idx + 1].islower():
                    if idx + 2 <= len(input):
                        input = input[:idx] + input[idx + 2:]
                    else:
                        input = input[:idx]
                else:
                    react_idx.remove(idx)
"""

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

@timer
def solve():
    input = read_file('05')[0]
    return len(react(input))

result = solve()
print(f'Solution: {result}')