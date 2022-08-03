from utils import read_file, timer

@timer
def solve():
    input = read_file("16")
    
    for row in input:
        elements = row.split(', ')
        data = {}
        for el in elements:
            temp, n = el.split(' ')

result = solve()
print(f'Solution: ')