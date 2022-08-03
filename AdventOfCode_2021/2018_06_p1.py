from utils import read_file, timer
from itertools import count




@timer
def solve():
    input = read_file("06")
    fishes = input.split(',')
    fishes = [int(fish) for fish in fishes]
    tot_days = 80
    for day in range(tot_days):
        for i in range(len(fishes)):
            if fishes[i] > 0:
                fishes[i] -= 1
            else:
                fishes[i] = 6
                fishes.append(8)

    return len(fishes)

result = solve()
print(f'Solution: {result}')