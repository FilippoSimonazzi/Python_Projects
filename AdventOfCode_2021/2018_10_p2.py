from utils import read_file, timer

PIECES = {'(': ')', '[': ']', '{': '}', '<': '>'}
VALUES = {')': 3, ']': 57, '}': 1197, '>': 25137,
          '(': 1, '[': 2, '{': 3, '<': 4}

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

def complete_line(line):
    tot = 0
    while len(line) > 0:
        tot *= 5
        tot += VALUES[line[-1]]
        line = line[:-1]
    return tot


@timer
def solve():
    input = read_file("10")
    incomplete_lines = []
    for line in input:
        shrinked_chunk = shrink_chunk(line)
        if all([True if ch in PIECES.keys() else False for ch in shrinked_chunk]):
            incomplete_lines.append(shrinked_chunk)
    scores = []
    for line in incomplete_lines:
        scores.append(complete_line(line))
    scores = sorted(scores)
    idx = len(scores) // 2
    return scores[idx]
    
result = solve()
print(f'Solution: {result}')