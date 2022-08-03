from utils import read_file, timer

@timer
def solve():
    input = read_file("13")


    #input = ['0: 3', '1: 2', '4: 4', '6: 4']


    data = {}
    for pos in input:
        p, d = list(map(int, pos.split(': ')))
        data[p] = {}
        data[p]['depth'] = d
        data[p]['current'] = 0
        data[p]['down'] = True
    
    current_pos = 0
    time = 0
    last_pos = int(input[-1].split(': ')[0])

    for pos in range(last_pos):
        if pos not in data.keys():
            data[pos] = {}
            data[pos]['depth'] = 0
            data[pos]['current'] = 0

    score = 0

    while current_pos <= last_pos:
        if data[current_pos]['current'] == 0:
            score += data[current_pos]['depth'] * current_pos
            #if data[current_pos]["depth"] > 0:
            #    print(f'Updated score! {current_pos = }, {data[current_pos]["depth"] = }, {score = }')
        for p in data.keys():
            if data[p]['depth'] > 0:
                if data[p]['down']:
                    data[p]['current'] = data[p]['current'] + 1
                    if data[p]['current'] == data[p]['depth'] - 1:
                        data[p]['down'] = False
                else:
                    data[p]['current'] = data[p]['current'] - 1
                    if data[p]['current'] == 0:
                        data[p]['down'] = True
        current_pos += 1
        time += 1

    return score
        



result = solve()
print(f'Solution: {result}')