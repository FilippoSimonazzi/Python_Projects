import re
from utils import read_file, timer, get_ints


def next(score_1, score_2, idx_1, idx_2, scoreboard):
    new_score = str(score_1 + score_2)
    if len(new_score) > 1:
        scoreboard.append(int(new_score[0]))
        scoreboard.append(int(new_score[1]))
    else:
        scoreboard.append(int(new_score))
    new_idx_1 = (idx_1 + score_1 + 1) % len(scoreboard)
    new_idx_2 = (idx_2 + score_2 + 1) % len(scoreboard)
    new_score_1 = scoreboard[new_idx_1]
    new_score_2 = scoreboard[new_idx_2]
    return new_score_1, new_score_2, new_idx_1, new_idx_2, scoreboard


@timer
def solve():
    input = get_ints(read_file("14"))[0]
    score_1, score_2 = 3, 7
    idx_1, idx_2 = 0, 1
    scoreboard = [score_1, score_2]
    while len(scoreboard) <= input + 10:
        score_1, score_2, idx_1, idx_2, scoreboard = next(score_1, score_2, idx_1, idx_2, scoreboard)

    final_scoreboard = [str(item) for item in scoreboard[input:input + 10]]
    return ''.join(final_scoreboard)

result = solve()
print(f'Solution: {result}')