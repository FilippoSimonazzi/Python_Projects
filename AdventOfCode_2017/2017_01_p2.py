from utils import read_file, timer

@timer
def solve():
    input = read_file("01")
    out = 0
    step = int(len(input) / 2)
    for i in range(len(input)):
        if input[i] == input[(i+step)%len(input)]:
            out += int(input[i])
    return out

result = solve()
print(f'Solution: {result}')