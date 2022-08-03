from utils import read_file, timer
from itertools import chain
from math import sqrt
from itertools import count

def divisors(n):
    return set(chain.from_iterable((i,n//i) for i in range(1,int(sqrt(n))+1) if n%i == 0))

def count_presents(n):
    div = list(divisors(n))
    tot = 0
    for d in div:
        tot += d * 10
    return tot

@timer
def solve():
    input = int(read_file("20"))
    for house in count(1):
        if count_presents(house) >= input:
            return house

result = solve()
print(f'Solution: {result}')