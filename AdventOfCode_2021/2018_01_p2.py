from utils import read_file, timer

@timer
def solve():
    input = read_file("01")
    tot = 0
    for i in range(len(input) - 3):
        window_1 = int(input[i]) + int(input[i+1]) + int(input[i+2])
        window_2 = int(input[i+1]) + int(input[i+2]) + int(input[i+3])
        if window_2 > window_1:
            tot +=1
    return tot
result = solve()
print(f'Solution: {result}')