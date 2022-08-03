from utils import read_file, timer


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.die = 0
        self.score = 0
        self.turn = 0
        self.win = False

    def play_turn(self):
        for _ in range(3):
            self.turn += 1
            self.die += self.turn
        self.pos = (self.pos + self.die) % 10
        if self.pos == 0:
            self.pos = 10
        self.score += self.pos
        if self.score >= 1000:
            self.win = True

@timer
def solve():
    input = read_file("21")
    players_pos, players_score = [], []
    for line in input:
        pos = int(line.split(' ')[-1])
        score = 0
        players_pos.append(pos)
        players_score.append(score)

    turn = 1
    player = 0
    rolls = 0
    while all(s < 1000 for s in players_score):
        die = 0
        for _ in range(3):
            if turn > 100:
                turn = 1
            die += turn
            turn += 1
            rolls += 1
        players_pos[player] = (players_pos[player] + die) % 10
        if players_pos[player] == 0:
            players_pos[player] = 10
        players_score[player] += players_pos[player]           
        player = (player + 1) % 2
    
    print(rolls, min(players_score))
    return min(players_score) * rolls

result = solve()
print(f'Solution: {result}')