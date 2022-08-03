from utils import read_file, timer

@timer
def solve():
    input = read_file("05")
    input = list(map(int, input))
    n_it = 0
    current_pos = 0
    while True:
        n_it += 1
        next_pos = current_pos + input[current_pos]
        input[current_pos] += 1
        current_pos = next_pos
        if next_pos >= len(input) or next_pos < 0:
            break
    return n_it
        
result = solve()
print(f'Solution: {result}')