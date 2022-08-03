import re
from utils import read_file, timer
from math import floor

class ALU:
    def __init__(self, n, instructions):
        self.values = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.n = n
        self.instructions = instructions
        self.idx = 0
        self.functions = {'add': self.add,
                          'mul': self.mul,
                          'div': self.div,
                          'mod': self.mod,
                          'eql': self.eql}

    def inp(self, a, N):
        self.values[a] = N
    
    def add(self, a, b):
        self.values[a] = self.values[a] + b
    
    def mul(self, a, b):
        self.values[a] = self.values[a] * b

    def div(self, a, b):
        self.values[a] = floor(self.values[a] / b)
    
    def mod(self, a, b):
        self.values[a] = self.values[a] % b

    def eql(self, a, b):
        self.values[a] = int(self.values[a] == b)

    def validate(self):
        for line in self.instructions:
            op = line.split(' ')[0]
            if op == 'inp':
                a = line.split(' ')[1]
                N = int(str(self.n)[self.idx])
                self.inp(a, N)
                self.idx += 1
            else:
                a, b = line.split(' ')[1:]
                if not b.lstrip('-').isdigit():
                    b = self.values[b]
                else:
                    b = int(b)
                self.functions[op](a, b)
        return self.values['z']
            
@timer
def solve():
    input = read_file("24")
    for n in range(10**14, 10**13, -1):
        if n % 100000 == 0:
            print(n)
        if '0' in str(n):
            continue
        alu = ALU(n, input)
        out = alu.validate()
        if out == 0:
            return n

result = solve()
print(f'Solution: {result}')