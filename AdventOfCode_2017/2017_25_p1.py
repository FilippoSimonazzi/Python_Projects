from utils import read_file, timer

def execute(states, state, pos, machine, active):
    instructions = states[state][int(active)]

    print(instructions, pos, active)
    print(machine)
    
    # write
    machine[pos] = int(instructions[0])

    print(machine)

    # move
    if instructions[1] == 'right':
        pos += 1
    if instructions[1] == 'left':
        pos -= 1
    if pos == -1:
        pos = 0

    print(pos)
    if pos != len(machine):
        machine.insert(pos, 0)
    else:
        machine.append(0)

    # new state
    state = instructions[2]

    print(machine, pos)
    print()
    return state, pos, machine



@timer
def solve():
    input = read_file("25")
    states = {}
    
    i = 3
    while i < len(input) - 1:
        if input[i][0] == 'I':
            state = input[i].split(' ')[-1][:-1]
            states[state] = {0: [], 1: []}
            for j in range(2, 5):
                idx = i + j
                if idx >= len(input):
                    break
                states[state][0].append(input[idx].split(' ')[-1][:-1])
            i += j
            for j in range(2, 5):
                idx = i + j
                if idx >= len(input):
                    break
                states[state][1].append(input[idx].split(' ')[-1][:-1])
            i += j
        i += 2

    state = input[0].split(' ')[-1][:-1]
    tot_steps = int(input[1].split(' ')[-2])

    n_it = 0
    machine = [0]
    pos = 0
    while n_it < tot_steps:
        n_it += 1
        state, pos, machine = execute(states, state, pos, machine, machine[pos])
        #print(n_it, machine)






result = solve()
print(f'Solution: ')