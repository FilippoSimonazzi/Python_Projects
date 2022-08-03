from utils import read_file, timer
from collections import defaultdict


N_SEG = {2: '1',
         3: '7',
         4: '4',
         5: ['2', '3', '5'],
         6: ['0', '6'],
         7: '8'
        }

def decode(inp, out):
    D = defaultdict(set)
    S = defaultdict(str)
    x = [None] * 7
    for seg in inp:
        if len(seg) in [2, 3, 4, 7]:
            chars = [ch for ch in seg]
            for ch in chars:
                D[len(seg)].add(ch)
        else:
            D[len(seg)].add(seg)
    D[5] = set(list(D[5])[0]) & set(list(D[5])[1]) & set(list(D[5])[2])
    D[6] = set(list(D[6])[0]) & set(list(D[6])[1]) & set(list(D[6])[2])
    x[0] = D[3] - D[2]
    x[1] = D[4] - D[3] - D[5]
    x[3] = D[4] - D[3] - x[1]
    x[6] = D[5] - x[0] - x[3]
    x[5] = D[6] - x[0] - x[1] - x[6]
    x[2] = D[2] - x[5]
    x[4] = D[7] - x[0] - x[1] - x[2] - x[3] - x[5] - x[6]
    sol = [list(el)[0] for el in x]
    
    indeces = [[0, 1, 2, 4, 5, 6], [2, 5], [0, 2, 3, 4, 6], [0, 2, 3, 5, 6], [1, 2, 3, 5],
           [0, 1, 3, 5, 6], [0, 1, 3, 4, 5, 6], [0, 2, 5], [x for x in range(7)], [0, 1, 2, 3, 5, 6]]

    for num, idx in enumerate(indeces):
        for ch in idx:
            S[num] += sol[ch]
        S[num] = set(S[num])

    
    decoded = ''
    for seg in out:
        for num in range(10):
            if set(seg) == S[num]:
                decoded += str(num)    
    return int(decoded)

@timer
def solve():
    input = read_file("08")
    inp = [x.split(' ')[:10] for x in input]
    out = [x.split(' ')[-4:] for x in input]
    tot = 0
    for i in range(len(input)):
        tot += decode(inp[i], out[i])
    return tot

result = solve()
print(f'Solution: {result}')