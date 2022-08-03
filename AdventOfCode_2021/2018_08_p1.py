from utils import read_file, timer

N_SEGMENTS = {1: 2,
              4: 4,
              7: 3,
              8: 7}

@timer
def solve():
    input = read_file("08")
    input = [x.split(' ')[-4:] for x in input]
    tot = 0
    for line in input:
        for el in line:
            if len(el) in N_SEGMENTS.values():
                tot += 1
    return tot

result = solve()
print(f'Solution: {result}')