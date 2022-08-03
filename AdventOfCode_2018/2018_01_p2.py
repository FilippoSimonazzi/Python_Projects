from utils import read_file, timer


@timer
def solve():
    input = [int(x) for x in read_file('01')]
    known = set()
    result = 0
    
    while True:
        for val in input:
            result += val
            if result in known:
                return result
            known.add(result)

result = solve()
print(f'Solution: {result}')