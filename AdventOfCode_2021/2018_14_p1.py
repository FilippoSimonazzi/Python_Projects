from utils import read_file, timer
from collections import deque, Counter
@timer
def solve():
    input = read_file("14")
    start, rules = input[0], input[2:]
    rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in rules}
    N = 10
    template = deque()
    for l in start:
        template.append(l)
    
    for _ in range(N):
        new_template = deque()
        for i in range(len(template) - 1):
            pair = template[i] + template[i+1]
            ins = rules[pair]
            new_template.append(template[i])
            new_template.append(ins)
        new_template.append(template.pop())
        template = new_template.copy()

    sol = Counter(template)
    return max(sol.values()) - min(sol.values())

result = solve()
print(f'Solution: {result}')