from utils import read_file, timer
from collections import defaultdict, Counter

def polymerise(P, R, steps):
    for _ in range(steps):
        NP = defaultdict[str](int)
        for pair, count in P.items():
            x, y = pair
            z = R[pair]
            NP[x + z] += count
            NP[z + y] += count
        P = NP
    return P

@timer
def solve():
    input = read_file("14")
    T, rules = input[0], input[2:]
    R = dict(r.split(' -> ') for r in rules)

    P = Counter([a+b for a,b in zip(T, T[1:])])

    P = polymerise(P, R, steps=40)
    
    sol = {}
    for c in set(''.join(P.keys())):
        sol[c] = max(sum(count for (p1, _), count in P.items() if c == p1),
                     sum(count for (_, p2), count in P.items() if c == p2))
    return max(sol.values()) - min(sol.values())

result = solve()
print(f'Solution: {result}')