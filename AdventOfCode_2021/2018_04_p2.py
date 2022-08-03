from utils import read_file, timer

def check_win(board):
    for row in board:
        if all(list(zip(*row))[1]):
            return True
    for col in list(zip(*board)):
        if all(list(zip(*col))[1]):
            return True


def compute_score(board, number):
    tot_unmarked = 0
    for row_idx in range(5):
        for col_idx in range(5):
            if not board[row_idx][col_idx][1]:
                tot_unmarked += board[row_idx][col_idx][0]
    return tot_unmarked * number


@timer
def solve():
    input = read_file("04")
    numbers = [int(x) for x in input[0].split(',')]
    boards = []
    new_board = []
    for i in range(2, len(input[1:]) + 1):
        if input[i] == '':
            boards.append(new_board)
            new_board = []
        else:
            row = [[int(x), False] for x in input[i].split()]
            new_board.append(row)

    boards.append(new_board)
    check_boards = [False] * len(boards)

    for number in numbers:
        for idx, board in enumerate(boards):
            for row_idx in range(5):
                for col_idx in range(5):
                    if board[row_idx][col_idx][0] == number:
                        board[row_idx][col_idx][1] = True
                        
                        if check_win(board):
                            check_boards[idx] = True
                            if all(check_boards):
                                return compute_score(board, number)
result = solve()
print(f'Solution: {result}')