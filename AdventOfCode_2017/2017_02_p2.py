from utils import read_file, timer

@timer
def solve():
    input = read_file("02")
    input = [x.replace('\t', ',') for x in input]

    out = 0
    for row in input:
        values = list(map(int, row.split(',')))
        for i in range(len(values)):
            for j in range(len(values)):
                if (i != j) and (values[i] % values[j] == 0):
                    out += int(values[i] / values[j])
                    break
    return out


result = solve()
print(f'Solution: {result}')