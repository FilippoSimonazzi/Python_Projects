from utils import read_file, timer
from collections import defaultdict

def roll_dice():
    dice_rolls = defaultdict(int)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                roll_total = d1 + d2 + d3
                dice_rolls[roll_total] += 1
    return dice_rolls

dice_rolls = roll_dice()

def play_game(games):
    global wins
    wins = [0, 0]
    while len(games) > 0:
        games_this_round = dict(games)
        games = defaultdict(int)
        for state, universes in games_this_round.items():
            game_round(state, universes, games)
    return wins


def game_round(game, universes, games):
    global wins
    (p1_pos, p1_score), (p2_pos, p2_score) = game

    # player 1
    for roll, univ_roll in dice_rolls.items():
        p1_universes = universes * univ_roll
        new_p1_pos = p1_pos + roll
        new_p1_pos = (new_p1_pos - 1) % 10 + 1
        new_p1_score = p1_score + new_p1_pos
        if new_p1_score >= 21:
            wins[0] += p1_universes
        else:

            # player 2
            for roll2, univ_roll2 in dice_rolls.items():
                p2_universes = p1_universes * univ_roll2
                new_p2_pos = p2_pos + roll2
                new_p2_pos = (new_p2_pos - 1) % 10 + 1
                new_p2_score = p2_score + new_p2_pos
                if new_p2_score >= 21:
                    wins[1] += p2_universes
                else:
                    new_state = ((new_p1_pos, new_p1_score), (new_p2_pos, new_p2_score))
                    games[new_state] += p2_universes
    return


@timer
def solve():
    position = [7, 3]
    games = defaultdict(int)
    state = ((position[0], 0), (position[1], 0))
    games[state] = 1
    
    wins = play_game(games)

    return wins, max(wins)

result = solve()
print(f'Solution: {result}')