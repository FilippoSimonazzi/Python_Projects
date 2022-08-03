from utils import read_file, timer
from collections import defaultdict
from functools import reduce
from operator import concat, ne

def determine_order(input):
    order = defaultdict(list)
    steps = set()
    for line in input:
        before, after = line.split()[1], line.split()[-3]
        order[before].append(after)
        steps.add(before)
        steps.add(after)
    return order, steps


def execute(input):
    order, steps = determine_order(input)
    result = ''
    while True:
        values = sum(order.values(), [])
        after_steps = set(values)
        if len(after_steps) == 0:
            break
        to_be_executed = list(steps - after_steps)
        if len(to_be_executed) > 0:
            next_step = sorted(to_be_executed)[0]
            for item in sorted(to_be_executed)[1:]:
                after_steps.add(item)
        else:
            next_step = to_be_executed[0]
        result += next_step

        steps = after_steps
        del order[next_step]

    result += list(steps)[0]
    return result

@timer
def solve():
    input = read_file("07")
    result = execute(input)
    return result

result = solve()
print(f'Solution: {result}')