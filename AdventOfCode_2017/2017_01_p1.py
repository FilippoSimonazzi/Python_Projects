from utils import read_file, timer

@timer
def solve():
    input = read_file("01")
    out = 0
    for i in range(len(input) - 1):
        if input[i] == input[i+1]:
            out += int(input[i])
    if input[-1] == input[0]:
        out += int(input[-1])
    return out

result = solve()
print(f'Solution: {result}')