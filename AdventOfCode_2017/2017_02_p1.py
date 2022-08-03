from utils import read_file, timer

@timer
def solve():
    input = read_file("02")
    input = [x.replace('\t', ',') for x in input]

    out = 0
    for row in input:
        values = list(map(int, row.split(',')))
        out += (max(values) - min(values))
    return out

result = solve()
print(f'Solution: {result}')