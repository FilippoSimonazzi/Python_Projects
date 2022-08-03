from utils import read_file, timer

PIECES = {'(': ')', '[': ']', '{': '}', '<': '>'}
VALUES = {')': 3, ']': 57, '}': 1197, '>': 25137}

def shrink_chunk(chunk):
    new_chunk = ''
    it = 0
    while new_chunk != chunk:
        if it > 0:
            chunk = new_chunk
            new_chunk = ''
        idx = 0
        while idx < len(chunk) - 1:
            if chunk[idx] in PIECES.keys():
                if chunk[idx + 1] != PIECES[chunk[idx]]:
                    new_chunk += chunk[idx]
                    idx += 1
                else:
                    idx += 2
            else:
                new_chunk += chunk[idx]
                idx += 1    
        if chunk[-2] in PIECES.keys():
            if chunk[-1] != PIECES[chunk[-2]]:
                new_chunk += chunk[-1]
        else:
            new_chunk += chunk[-1]
        it += 1
    return new_chunk


@timer
def solve():
    input = read_file("10")
    tot = 0
    for line in input:
        shrinked_chunk = shrink_chunk(line)
        if not all([True if ch in PIECES.keys() else False for ch in shrinked_chunk]):
            for ch in shrinked_chunk:
                if ch not in PIECES.keys():
                    tot += VALUES[ch]
                    break
    return tot

result = solve()
print(f'Solution: {result}')