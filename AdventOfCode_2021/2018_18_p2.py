import re
from utils import read_file, timer
from math import ceil


class Snail:
    def __init__(self, value, y):
        self.y = y
        self.value = value
    
    def __str__(self):
        return f'{self.value}: {self.y}'

def parse_snale_to_alt_representation(snail):
    snail = str(snail)
    snail_list = []
    y_index, number = 0, ''
    for letter in snail:
        if letter == '[':
            y_index += 1
        elif letter == ']':
            if number != '':
                snail_list.append(Snail(int(number), y_index))
                number = ''
            y_index -= 1
        elif letter == ',':
            if number != '':
                snail_list.append(Snail(int(number), y_index))
                number = ''
        elif letter != ' ':
            number += letter
    return snail_list


def check_and_explode(snail):
    for i in range(len(snail) - 1):
        if 4 < snail[i].y == snail[i+1].y:
            if i > 0:
                snail[i-1].value += snail[i].value
            if i + 2 < len(snail):
                snail[i+2].value += snail[i+1].value
            snail[i] = Snail(0, snail[i].y - 1)
            snail.pop(i + 1)
            return True
    return False

def check_and_split(snail):
    for i in range(len(snail)):
        if snail[i].value >= 10:
            snail_half = snail[i].value / 2
            snail_left = int(snail_half)
            snail_right = ceil(snail_half)
            snail[i].value = snail_left
            snail[i].y = snail[i].y + 1
            snail.insert(i + 1, Snail(snail_right, snail[i].y))
            return True
    return False

def reduce_snailfish(snail):
    while True:
        if check_and_explode(snail):
            continue
        elif check_and_split(snail):
            continue
        break
    return snail

def add_snails(snail1, snail2):
    snail_res = snail1 + snail2
    for snail in snail_res:
        snail.y = snail.y + 1
    snail_res = reduce_snailfish(snail_res)
    return snail_res

def get_magnitude(snail):
    while len(snail) > 1:
        for i in range(len(snail) - 1):
            if snail[i].y == snail[i+1].y:
                snail[i].value = snail[i].value * 3 + snail[i+1].value * 2
                snail[i].y -= 1
                snail.pop(i+1)
                break
    return snail[0].value

@timer
def solve():
    input = read_file("18")
    input = [eval(x) for x in input]
    
    sol = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if i != j:
                snail1 = parse_snale_to_alt_representation(input[i])
                snail2 = parse_snale_to_alt_representation(input[j])
                magnitude = get_magnitude(add_snails(snail1, snail2))
                sol = max(sol, magnitude)
    
    return sol
result = solve()
print(f'Solution: {result}')