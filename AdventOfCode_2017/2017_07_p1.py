from utils import read_file, timer

@timer
def solve():
    input = read_file("07")
    data = []
    for row in input:
        row = row.split(' ')
        if len(row) > 2:
            data.append((row[0], row[1].strip('()'), *row[3:]))
        else:
            data.append((row[0], row[1].strip('()')))
    
    used = set()
    keys = set()
    for row in data:
        if len(row) > 2:
            keys.add(row[0])
            for i in range(2, len(row)):
                used.add(row[i].strip(','))
    
    return list((keys - keys.intersection(used)))[0]

result = solve()
print(f'Solution: {result}')