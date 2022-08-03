from utils import read_file, timer

@timer
def solve():
    input = read_file("09")
    removed = 0
    tot_garbage = 0
    i = 0
    in_garbage = False
    while i < len(input):
        if in_garbage:
            tot_garbage += 1
        if input[i] == '<':
            if not in_garbage:
                in_garbage = True
            else:
                removed += 1
        elif input[i] == '>' and in_garbage:
            in_garbage = False
        elif input[i] == '!' and in_garbage:
            i += 1
        else:
            if in_garbage:
                removed += 1

        i += 1

    #return tot_garbage - removed
    return removed

result = solve()
print(f'Solution: {result}')