from utils import read_file, timer

weapons = {
    'Dagger': {'cost': 8, 'damage': 4, 'armor': 0},
    'Shortsword': {'cost': 10, 'damage': 5, 'armor': 0},
    'Warhammer': {'cost': 25, 'damage': 6, 'armor': 0},
    'Longsword': {'cost': 40, 'damage': 7, 'armor': 0},
    'Greataxe': {'cost': 74, 'damage': 8, 'armor': 0}
}

armors = {
    'Leather': {'cost': 13, 'damage': 0, 'armor': 1},
    'Chainmail': {'cost': 31, 'damage': 0, 'armor': 2},
    'Splintmail': {'cost': 53, 'damage': 0, 'armor': 3},
    'Bandedmail': {'cost': 75, 'damage': 0, 'armor': 4},
    'Platemail': {'cost': 102, 'damage': 0, 'armor': 5},
}

rings = {}


class Player():
    def __init__(self):
        self.damage_score = 0
        self.armor = 0
        self.item = None

@timer
def solve():
    input = read_file("21")
    pass

result = solve()
print(f'Solution: ')