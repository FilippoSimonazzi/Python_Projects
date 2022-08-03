from utils import read_file, timer
from collections import defaultdict
import operator

@timer
def solve():
    input = read_file("08")
    register = defaultdict(int)
    max_value = 0

    for row in input:
        action, cond = row.split(' if ')
        
        # check condition
        cond = cond.split(' ')
        letter = cond[0]
        if letter not in register.keys():
            register[letter] = 0
        
        cond[0] = 'register[letter]'
        cond = ' '.join(cond)

        if eval(cond):
            # activate the action
            letter, operation, number = action.split(' ')
            number = int(number)
            if operation == 'inc':
                register[letter] += number
            elif operation == 'dec':
                register[letter] -= number

        if max(register.values()) > max_value:
            max_value = max(register.values())
            
    return max_value

result = solve()
print(f'Solution: {result}')


