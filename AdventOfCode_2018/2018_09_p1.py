from utils import get_ints, read_file, timer
from collections import deque


@timer
def solve():
    players, last_marble = get_ints(read_file('09'))
    last_marble *= 100
    scores = [0] * players
    field = deque([0])
    
    for current_marble in range(1, last_marble + 1):
        if not current_marble % 23:
            field.rotate(7)
            scores[current_marble % players] += current_marble + field.pop()
            field.rotate(-1)
        else:
            field.rotate(-1)
            field.append(current_marble)
    
    return max(scores)


result = solve()
print(f'Solution: {result}')