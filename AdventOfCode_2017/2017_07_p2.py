from utils import read_file, timer

@timer
def solve():
    input = read_file("07")
    data = []
    for row in input:
        row = row.split(' ')
        if len(row) > 2:
            to_append = [row[0], int(row[1].strip('()'))]
            for i in range(3, len(row)):
                to_append.append(row[i].strip(','))
            data.append(to_append)
        else:
            data.append((row[0], int(row[1].strip('()'))))

    weights = {}
    for row in data:
        weights[row[0]] = row[1]
    
    print(weights)
result = solve()
print(f'Solution: {result}')