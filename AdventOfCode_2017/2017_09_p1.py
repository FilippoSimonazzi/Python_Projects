from utils import read_file, timer

@timer
def solve():
    input = read_file("09")

    score = 0
    i = 0
    in_garbage = False
    open_groups = 0
    while i < len(input):
        if input[i] == '{' and not in_garbage:
            open_groups += 1
        elif input[i] == '}' and not in_garbage:
            score += open_groups
            open_groups -= 1
        elif input[i] == '<' and not in_garbage:
            in_garbage = True
        elif input[i] == '>' and in_garbage:
            in_garbage = False
        
        if input[i] == '!':
            i += 1
        i += 1

    return score

result = solve()
print(f'Solution: {result}')