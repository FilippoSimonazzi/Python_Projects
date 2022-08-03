from utils import read_file, timer
from collections import deque

@timer
def solve():
    input = 382
    N = 50000000
    buffer = deque([0])
    for i in range(1, N+1):
        buffer.rotate(-input-1)
        buffer.appendleft(i)
    
    buffer.popleft()
    return buffer.popleft()

result = solve()
print(f'Solution: {result}')