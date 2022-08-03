from utils import read_file, timer
from collections import defaultdict
from string import ascii_lowercase

def spin(l, n):
    return l[-n:] + l[:-n]

def exchange(l, a, b):
    temp = []
    for letter in l:
        temp.append(letter)
    temp[a], temp[b] = temp[b], temp[a]
    l = ''.join(temp)
    return l

def partner(l, a, b):
    idx_a = l.index(a)
    idx_b = l.index(b)
    return exchange(l, idx_a, idx_b)

@timer
def solve():
    input = read_file("16").split(',')
    
    word = ascii_lowercase[:16]
    
    for _ in range(10**9):
        old_word = word
        for action in input:
            if action[0] == 'x':
                action = list(map(int, action[1:].split('/')))
                word = exchange(word, *action)
            
            elif action[0] == 'p':
                action = action[1:].split('/')
                word = partner(word, *action)
            
            elif action[0] == 's':
                word = spin(word, int(action[1:]))

        if old_word == word:
            break

    return word



result = solve()
print(f'Solution: {result}')