from utils import read_file, timer
from collections import defaultdict

class garden:
    def __init__(self, initial_state, key_input):
        self.generation = 0
        self.first_idx = 0
        self.state = initial_state.split(' ')[-1]
        self.keys = defaultdict(lambda: '.')
        for keystr in key_input:
            key, value = map(str.strip, keystr.split('='))
            self.keys[key] = value[-1]
        
    def grow(self):
        pass
        



@timer
def solve():
    input = read_file("12")
    pass

result = solve()
print(f'Solution: {result}')