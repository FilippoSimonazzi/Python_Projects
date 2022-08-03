from collections import defaultdict
from utils import read_file, timer

def read_input(inp):
    bots = defaultdict(list)
    outputs = defaultdict(list)
    for row in inp:
        row = row.split()
        if row[0] == 'value':
            bot_num = row[-1]
            val = int(row[1])
            bots[bot_num].append(val)
    for row in inp:
        row = row.split()
        if row[0] == 'bot':
            bot_giver = row[1]
            low_receiver = row[5]
            low_num = row[6]
            high_receiver = row[-2]
            high_num = row[-1]

            low_value = min(bots[bot_giver])
            high_value = max(bots[bot_giver])

            if low_receiver == 'bot':
                bots[low_num].append(low_value)
            else:
                outputs[low_num].append(low_value)
            bots[bot_giver].remove(low_value)

            if high_receiver == 'bot':
                bots[high_num].append(high_value)
            else:
                outputs[high_num].append(high_value)
            bots[bot_giver].remove(high_value)

    return bots, outputs
            

@timer
def solve():
    input = read_file("10")
    bots, outputs = read_input(input)

    print(bots)
    print(outputs)

result = solve()
print(f'Solution: ')