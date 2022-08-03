from utils import read_file, timer

@timer
def solve():
    input = read_file("11").split(',')

    max_dist = 0
    pos = [0, 0] # west, nord
    for move in input:
        if move == 'n':
            pos[1] += 1
        elif move == 's':
            pos[1] -= 1
        elif move == 'nw':
            pos[0] += 0.5
            pos[1] += 0.5
        elif move == 'ne':
            pos[0] -= 0.5
            pos[1] += 0.5
        elif move == 'sw':
            pos[0] += 0.5
            pos[1] -= 0.5
        elif move == 'se':
            pos[0] -= 0.5
            pos[1] -= 0.5

        current_dist = int(abs(pos[0]) + abs(pos[1]))
        if current_dist > max_dist:
            max_dist = current_dist
    
    return max_dist

result = solve()
print(f'Solution: {result}')