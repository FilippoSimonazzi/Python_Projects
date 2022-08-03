from utils import read_file, timer

@timer
def solve():
    input = read_file("01")
    tot = 0
    for i in range(len(input) - 1):
        if int(input[i+1]) > int(input[i]):
            tot += 1
    return tot

result = solve()
print(f'Solution: {result}')