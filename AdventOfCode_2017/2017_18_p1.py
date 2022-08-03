from utils import read_file, timer
from string import ascii_lowercase
from collections import defaultdict

@timer
def solve():
    input = read_file("18")
    registers_1 = dict()
    registers_2 = dict()

    i = 0
    while i in range(len(input)) and j in range(len(input)):
        row = input[i].split(' ')
        if len(row) == 2:
            ins, reg = row[0], row[1]
        elif len(row) == 3:
            ins, reg, val = row[0], row[1], row[2]

        if reg not in registers_1.keys():
            registers_1[reg] = 0
        if reg not in registers_2.keys():
            registers_2[reg] = 0

        if ins == 'set':
            if val not in ascii_lowercase:
                registers_1[reg] = int(val)
                registers_2[reg] = int(val)
            else:
                registers_1[reg] = registers_1[val]
                registers_2[reg] = registers_2[val]
        elif ins == 'add':
            if val not in ascii_lowercase:
                registers_1[reg] += int(val)
                registers_2[reg] += int(val)
            else:
                registers_1[reg] += registers_1[val]
                registers_2[reg] += registers_2[val]
        elif ins == 'mul':
            if val not in ascii_lowercase:
                registers_1[reg] *= int(val)
                registers_2[reg] *= int(val)
            else:
                registers_1[reg] *= registers_1[val]
                registers_2[reg] *= registers_2[val]
        elif ins == 'mod':
            if val not in ascii_lowercase:
                registers_1[reg] %= int(val)
                registers_2[reg] %= int(val)
            else:
                registers_1[reg] %= registers_1[val]
                registers_2[reg] %= registers_2[val]
        elif ins == 'jgz':
            if registers_1[reg] > 0:
                if val not in ascii_lowercase:
                    i += int(val) - 1
                else:
                    i += registers_1[val] - 1
            if registers_2[reg] > 0:
                if val not in ascii_lowercase:
                    i += int(val) - 1
                else:
                    i += registers_1[val] - 1
        elif ins == 'snd':
            sound = registers[reg]
        elif ins == 'rcv':
            if registers[reg] > 0:
                return sound
        i += 1        


    return 'FINISHED WITHOUT SOUND'
                


result = solve()
print(f'Solution: {result}')