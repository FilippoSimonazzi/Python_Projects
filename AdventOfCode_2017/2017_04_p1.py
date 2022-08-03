from utils import read_file, timer

@timer
def solve():
    input = read_file("04")
    tot = 0
    for row in input:
        row = row.split(' ')
        used = set()
        valid = True
        for word in row:
            if word in used:
                valid = False
                break
            else:
                used.add(word)
        if valid:
            tot += 1
    return tot

result = solve()
print(f'Solution: {result}')