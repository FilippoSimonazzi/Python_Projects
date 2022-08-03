from utils import read_file, timer
from collections import defaultdict

@timer
def solve():
    input = read_file("03")
    idx_oxygen, idx_co2 = set([x for x in range(len(input))]), set([x for x in range(len(input))])
    current_bit = 0

    while len(idx_oxygen) > 1:
        check_input = list(zip(*[input[i] for i in range(len(input)) if i in idx_oxygen]))
        position = sorted(check_input[current_bit])[::-1]
        num = max(position, key=position.count)

        for i in range(len(input)):
            if i not in idx_oxygen:
                continue
            if input[i][current_bit] != num:
                idx_oxygen.remove(i)
        
        current_bit += 1
    
    current_bit = 0
    while len(idx_co2) > 1:
        check_input = list(zip(*[input[i] for i in range(len(input)) if i in idx_co2]))
        position = sorted(check_input[current_bit])
        num = min(position, key=position.count)

        for i in range(len(input)):
            if i not in idx_co2:
                continue
            if input[i][current_bit] != num:
                idx_co2.remove(i)
        
        current_bit += 1
    
    oxygen = int(input[list(idx_oxygen)[0]], 2)
    co2 = int(input[list(idx_co2)[0]], 2)
    return oxygen * co2

result = solve()
print(f'Solution: {result}')
