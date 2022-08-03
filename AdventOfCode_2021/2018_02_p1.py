from utils import read_file, timer

@timer
def solve():
    input = read_file("02")
    pos = [0, 0]
    for line in input:
        if line.split()[0] == 'forward':
            pos[0] += int(line.split()[1])
        elif line.split()[0] == 'down':
            pos[1] += int(line.split()[1])
        elif line.split()[0] == 'up':
            pos[1] -= int(line.split()[1])
    return pos[0] * pos[1]

result = solve()
print(f'Solution: {result}')