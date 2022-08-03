from utils import read_file, timer
from itertools import chain
from math import sqrt
from itertools import count
from collections import defaultdict

def divisors(n):
    return set(chain.from_iterable((i,n//i) for i in range(1,int(sqrt(n))+1) if n%i == 0))

def count_presents(n, count_div):
    div = list(divisors(n))
    tot = 0
    for d in div:
        count_div[d] += 1
        if count_div[d] > 50:
            continue
        tot += d * 11
    return tot, count_div

@timer
def solve():
    input = int(read_file("20"))
    count_div = defaultdict(int)
    for house in count(1):
        tot, count_div = count_presents(house, count_div)
        if tot >= input:
            return house

result = solve()
print(f'Solution: {result}')