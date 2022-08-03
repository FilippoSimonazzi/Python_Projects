from re import T
from utils import read_file, timer
from collections import defaultdict


def read_input(input):
    clay = []
    for line in input:
        if line.split(', ')[0][0] == 'x':
            x = int(line.split(', ')[0].split('=')[-1])
            y_min, y_max = line.split(', ')[1].split('=')[-1].split('..')
            y_min, y_max = int(y_min), int(y_max)
            for y in range(y_min, y_max + 1):
                clay.append((x, y))

        else:
            y = int(line.split(', ')[0].split('=')[-1])
            x_min, x_max = line.split(', ')[1].split('=')[-1].split('..')
            x_min, x_max = int(x_min), int(x_max)
            for x in range(x_min, x_max + 1):
                clay.append((x, y))

    field = defaultdict(str)
    source = (500, 0)
    field[(source[0], source[1])] = '+'
    for point in clay:
        field[(point[0], point[1])] = '#'
    
    min_x = min(field.keys(), key=lambda t:t[0])[0] - 10
    min_y = min(field.keys(), key=lambda t:t[1])[1]
    max_x = max(field.keys(), key=lambda t:t[0])[0] + 10
    max_y = max(field.keys(), key=lambda t:t[1])[1]
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in field.keys():
                field[(x, y)] = '.'
    return field
    
def print_field(field):
    min_x = min(field.keys(), key=lambda t:t[0])[0]
    min_y = min(field.keys(), key=lambda t:t[1])[1]
    max_x = max(field.keys(), key=lambda t:t[0])[0]
    max_y = max(field.keys(), key=lambda t:t[1])[1]
    grid = [[field[(x, y)] for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
    for i in range(len(grid)):
        print(grid[i])
        print()


def water_flow(field, verbose=False):
    water_position = [500, 2]
    previous_water_position = [500, 1]
    flow = True
    hit_wall = False
    while flow:
        field[tuple(water_position)] = 'X'
        field[tuple(previous_water_position)] = '|'

        if verbose:
            print(f'Hit Wall: {hit_wall}\n')
            print_field(field)
            print('\n\n\n')
        
        if field[water_position[0], water_position[1] + 1] == '.':
            field[tuple(previous_water_position)] = '.'
            previous_water_position = water_position.copy()
            water_position[1] += 1
            continue
        else:
            if not hit_wall:
                if field[water_position[0] + 1, water_position[1] + 1] in ['.', '|', '~']:
                    field[tuple(previous_water_position)] = '.'
                    previous_water_position = water_position.copy()
                    water_position[0] += 1
                    continue
                elif field[water_position[0] + 1, water_position[1]] == '#':
                    hit_wall = True
                    if field[water_position[0] - 1, water_position[1]] == '|':
                        field[tuple(previous_water_position)] = '='
                        previous_water_position = water_position.copy()
                        water_position[0] -= 1
                        continue
                elif field[water_position[0] - 1, water_position[1]] in ['.', '|', '~']:
                    field[tuple(previous_water_position)] = '.'
                    previous_water_position = water_position.copy()
                    water_position[0] -= 1
                    continue

                elif field[water_position[0] - 1, water_position[1]] == '#':
                    hit_wall = True
                    if field[water_position[0] + 1, water_position[1]] == '|':
                        field[tuple(previous_water_position)] = '='
                        previous_water_position = water_position.copy()
                        water_position[0] += 1
                        continue
            else:
                if field[water_position[0] + 1, water_position[1] + 1] == '.':
                    field[tuple(previous_water_position)] = '.'
                    previous_water_position = water_position.copy()
                    water_position[0] += 1
                    continue
                elif field[water_position[0] - 1, water_position[1]] == '.':
                    field[tuple(previous_water_position)] = '.'
                    previous_water_position = water_position.copy()
                    water_position[0] -= 1
                    continue
                else:
                    field[tuple(water_position)] = '~'
                    field[tuple(previous_water_position)] = '.'
                    flow = False

    return(field)

@timer
def solve():
    input = read_file('17')
    field = read_input(input)
    for i in range(15):
        if i == 14:
            field = water_flow(field, verbose=True)
        else:
            field = water_flow(field)
    print_field(field)

result = solve()
print(f'Solution: {result}')