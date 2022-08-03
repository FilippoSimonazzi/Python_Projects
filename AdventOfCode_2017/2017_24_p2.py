from matplotlib.style import available
from utils import read_file, timer


def run(b, d):
    available = [a for a in d if b[1] in a]
    if len(available) == 0:
        yield b
    else:
        for a in available:
            d_ = d.copy()
            d_.remove(a)
            for q in run((b[0] + [a], a[0] if b[1] == a[1] else a[1]), d_):
                yield q


@timer
def solve():
    input = read_file("24")
    data = []
    for row in input:
        data.append(tuple(map(int, row.split('/'))))

    bridge = ([], 0)


    max_length = max(map(lambda bridge: len(bridge[0]), run(bridge, data)))
    long = filter(lambda bridge: len(bridge[0]) == max_length, run(bridge, data))
    return max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), long))


result = solve()
print(f'Solution: {result}')