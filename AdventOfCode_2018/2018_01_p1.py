from utils import read_file, timer


@timer
def solve():
    input = read_file('01')
    frequencies = [int(x) for x in input]
    return sum(frequencies)


result = solve()
print(f'Solution: {result}')