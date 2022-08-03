import sys, itertools, collections
from utils import read_file, timer


def step(board):
    N, M = len(board), len(board[0])
    result = [[None]*M for i in range(N)]

    for i in range(N):
        for j in range(M):
            counts = collections.Counter()
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    i2, j2 = i + dx, j + dy
                    if 0 <= i2 < N and 0 <= j2 < M:
                        counts[board[i2][j2]] += 1
            if board[i][j] == '.':
                result[i][j] = '|' if counts['|'] >= 3 else '.'
            elif board[i][j] == '|':
                result[i][j] = '#' if counts['#'] >= 3 else '|'
            else:
                result[i][j] = '#' if (counts['#'] >= 1 and counts['|'] >= 1) else '.'
    
    return result
                    

@timer
def solve():
    input = read_file("18")
    board = []
    for line in input:
        board.append(line)
    minutes = 1000000000
    for i in range(1, minutes + 1):
        board = step(board)
    counts = collections.Counter()
    for row in board:
        for c in row:
            counts[c] += 1
    return counts['#'] * counts['|']
        

result = solve()
print(f'Solution: {result}')