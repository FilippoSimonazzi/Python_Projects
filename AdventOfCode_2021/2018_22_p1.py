from utils import read_file, timer
from collections import defaultdict

def read_input(input):
    data = {}
    for idx, line in enumerate(input):
        action = line.split(' ')[0]
        x, y, z = line.split(',')
        x_start, x_end = x.split('=')[1].split('..')
        y_start, y_end = y.split('=')[1].split('..')
        z_start, z_end = z.split('=')[1].split('..')
        data[idx] = {'action': action, 
                    'x': (int(x_start), int(x_end)+1),
                    'y': (int(y_start), int(y_end)+1),
                    'z': (int(z_start), int(z_end)+1),
                    }
    return data

@timer
def solve():
    input = read_file("22")
    cubes = defaultdict(int)
    data = read_input(input)

    for ins in data.values():
        N = 50
        X = [x for x in range(max(-N, ins['x'][0]), min(N+1, ins['x'][1]))]
        Y = [y for y in range(max(-N, ins['y'][0]), min(N+1, ins['y'][1]))]
        Z = [z for z in range(max(-N, ins['z'][0]), min(N+1, ins['z'][1]))]

        for x in X:
            for y in Y:
                for z in Z:
                    cubes[(x, y, z)] = 1 if ins['action'] == 'on' else 0

    return sum(cubes.values())

result = solve()
print(f'Solution: {result}')