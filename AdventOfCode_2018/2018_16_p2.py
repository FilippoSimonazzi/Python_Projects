from os import defpath
from utils import read_file, timer
from itertools import compress
from collections import defaultdict

def addr(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] + register[B]
    return new_register

def addi(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] + B
    return new_register

def mulr(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] * register[B]
    return new_register

def muli(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] * B
    return new_register

def banr(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] & register[B]
    return new_register

def bani(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] & B
    return new_register

def borr(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] | register[B]
    return new_register

def bori(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A] | B
    return new_register

def setr(register, A, B, C):
    new_register = register.copy()
    new_register[C] = register[A]
    return new_register

def seti(register, A, B, C):
    new_register = register.copy()
    new_register[C] = A
    return new_register

def gtir(register, A, B, C):
    new_register = register.copy()
    if A > register[B]:
        new_register[C] = 1
    else:
        new_register[C] = 0
    return new_register

def gtri(register, A, B, C):
    new_register = register.copy()
    if register[A] > B:
        new_register[C] = 1
    else:
        new_register[C] = 0
    return new_register

def gtrr(register, A, B, C):
    new_register = register.copy()
    if register[A] > register[B]:
        new_register[C] = 1
    else:
        new_register[C] = 0
    return new_register

def eqir(register, A, B, C):
    new_register = register.copy()
    if A == register[B]:
        new_register[C] = 1
    else:
        new_register[C] = 0
    return new_register

def eqri(register, A, B, C):
    new_register = register.copy()
    if register[A] == B:
        new_register[C] = 1
    else:
        new_register[C] = 0
    return new_register

def eqrr(register, A, B, C):
    new_register = register.copy()
    if register[A] == register[B]:
        new_register[C] = 1
    else:
        new_register[C] = 0
    return new_register

funcs = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
}


def read_input(input):
    instructions = []
    i = 0
    while i < len(input):
        before = [int(x) for x in input[i].split(': [')[-1][:-1].split(', ')]
        command = [int(x) for x in input[i + 1].split()]
        after = [int(x) for x in input[i + 2].split(':  [')[-1][:-1].split(', ')]
        i += 4
        instructions.append((before, command, after))
    return instructions


def test(instruction, funcs):
    before = instruction[0]
    code, A, B, C = instruction[1]
    after = instruction[2]
    output = []
    for key in funcs.keys():
        tmp_register = funcs[key].__call__(before, A, B, C)
        if tmp_register == after:
            output.append(key)
    return code, output

@timer
def solve():
    result = 0
    input = read_file("16_1")
    instructions = read_input(input)
    codes = defaultdict(set)
    for key in range(16):
        codes[key] = set([x for x in range(16)])

    for i in range(len(instructions)):
        code, output = test(instructions[i], funcs)
        true_idx = set([i for i, x in enumerate(output) if x])
        codes[code] = codes[code].intersection_update(true_idx)

    print(codes)
    final_codes = defaultdict(int)
    #while not all([len(item) == 1 for item in codes.values()]):
    for i in range(4):
        keys_to_delete, values_to_delete = [], []
        for key, item in codes.items():
            if len(item) == 1:
                final_codes[key] = list(item)[0]
                keys_to_delete.append(key)
                values_to_delete.append(list(item)[0])
        for key in keys_to_delete:
            del codes[key]
        for value in values_to_delete:
            for key, item in codes.items():
                if value in item:
                    print(key, codes[key])
                    codes[key] -= {value}
                
        print(final_codes)
    return result

result = solve()
print(f'Solution: {result}')