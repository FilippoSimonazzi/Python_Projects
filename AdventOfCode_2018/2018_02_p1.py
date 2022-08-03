from os import read
from utils import read_file, timer


def count_letters(word):
    letters = set(word)
    same_two = False
    same_three = False
    for l in letters:
        if word.count(l) == 2:
            same_two = True
        elif word.count(l) == 3:
            same_three = True
        if same_two and same_three:
            return True, True
    return same_two, same_three

@timer
def solve():
    input = read_file('02')
    count_two, count_three = 0, 0
    for word in input:
        same_two, same_three = count_letters(word)
        if same_two:
            count_two += 1
        if same_three:
            count_three += 1
    return count_two * count_three

result = solve()
print(f'Solution: {result}')
    
    
