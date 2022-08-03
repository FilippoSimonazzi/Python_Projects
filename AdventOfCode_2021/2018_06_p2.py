from utils import read_file, timer
from collections import defaultdict, Counter

@timer
def solve():
    input = read_file("06")
    fishes = input.split(',')
    fishes = [int(fish) for fish in fishes]
    same_age = Counter(fishes)
    fishes_by_age = same_age.most_common()
    tot_days = 256

    for _ in range(tot_days):
        next_fishes = defaultdict[int, int](int, fishes_by_age)
        
        for age, total_fishes in fishes_by_age:
            week_ended = age == 0
            new_age = 6 if week_ended else (age - 1)
            next_fishes[new_age] += total_fishes
            next_fishes[age] -= total_fishes

            if week_ended:
                next_fishes[8] += total_fishes
            
        fishes_by_age = list(next_fishes.items())
    
    return sum(list(zip(*fishes_by_age))[1])


result = solve()
print(f'Solution: {result}')