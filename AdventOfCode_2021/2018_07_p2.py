from utils import read_file, timer
from collections import defaultdict

@timer
def solve():
    input = read_file("07").split(',')
    positions = [int(pos) for pos in input]

    fuel = defaultdict(int)
    for final_pos in range(min(positions), max(positions)+1):
        for pos in positions:
            fuel[final_pos] += sum(range(abs(pos - final_pos)+1))
    
    return fuel[min(fuel, key=fuel.get)]

result = solve()
print(f'Solution: {result}')