from utils import read_file, timer
from collections import defaultdict

class Field:
    def __init__(self, input):
        self.field = [[input[i][j] for j in range(len(input[i]))] for i in range(len(input))]
        self.N = len(self.field[0])


    def nb9(self, x, y):
        out = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i >= 0 and x + i < self.N:
                    if y + j >= 0 and y + j < self.N:
                        out.append(self.field[x + i][y + j])
        return out


    def update_point(self, x, y):
        state, around = self.new_state[(x, y)]
        
        # open --> tree
        if state == '.' and around.count('|') >= 3:
            return '|'
        
        # tree --> lumberyard
        if state == '|' and around.count('#') >= 3:
            return '#'

        # lumberyard --> lumberyard / open
        if state == '#':
            if around.count('#') >= 2 and around.count('|') >= 1:
                return '#'
            else:
                return '.'
        return state


    def update_field(self):
        self.new_state = defaultdict(list)
        for x in range(self.N):
            for y in range(self.N):
                self.new_state[(x, y)] = [self.field[x][y], self.nb9(x, y)]

        for x in range(self.N):
            for y in range(self.N):
                self.field[x][y] = self.update_point(x, y)

    def print_field(self):
        for i in range(self.N):
            print(self.field[i])
            print()

    
    def get_result_part_1(self):
        trees, lumberyards = 0, 0
        for x in range(self.N):
            for y in range(self.N):
                if self.field[x][y] == '|':
                    trees += 1
                elif self.field[x][y] == '#':
                    lumberyards += 1
        return trees * lumberyards

@timer
def solve():
    input = read_file("18")
    field = Field(input)
    minutes = 1000000000
    for _ in range(minutes):
        field.update_field()
    return field.get_result_part_1()

result = solve()
print(f'Solution: {result}')