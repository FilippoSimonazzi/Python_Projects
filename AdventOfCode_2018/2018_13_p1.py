from utils import read_file, timer


class Cart:
    def __init__(self, row, col, direction, grid):
        self.turn_step = 0
        self.row = row
        self.column = col
        self.current_position = [self.row, self.column]
        self.direction = direction
        self.original_grid = grid
       
    
    def new_position(self):
        if self.direction == '^':
            self.next_position = [self.row - 1, self.column]
        elif self.direction == 'v':
            self.next_position = [self.row + 1, self.column]
        elif self.direction == '>':
            self.next_position = [self.row, self.column + 1]
        elif self.direction == '<':
            self.next_position = [self.row, self.column - 1]

    def take_step(self):
        self.new_grid = self.original_grid.copy()
        if self.original_grid[self.next_position] in ['-', '|']:
            self.new_grid[self.next_position] = self.direction
            


        

@timer
def solve():
    input = read_file("13")
    X = len(input)
    Y = max([len(input[i]) for i in range(X)])
    grid = [[' ' for y in range(Y)] for x in range(X)]
    carts = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            piece = input[i][j]
            grid[i][j] = piece
            if piece in ['>', 'v', '^', '<']:
                carts.append(Cart(i, j, piece, grid))

    pass

result = solve()
print(f'Solution: ')