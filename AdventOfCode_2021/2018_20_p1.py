from utils import read_file, timer

def process(data):
    divide = data.index('')
    algo_img = ''.join(data[:divide])
    input_img = data[divide+1:]
    input_img = [[1 if x=='#' else 0 for x in row] for row in input_img]
    input_img = {(x, y): v for x, l in enumerate(input_img) for y, v in enumerate(l)}
    return algo_img, input_img


def display_img(img):
    first_row = list(img.keys())[0][0]
    last_row = list(img.keys())[-1][0]
    for r in range(first_row, last_row+1):
        values = ['#' if img[x] else '.' for x in img.keys() if x[0] == r]
        print((''.join(values)).center(last_row + 5, '.'))

def get_neigh_values(img, x, y):
    tot = ''
    check = False
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            temp_x = x + dx
            temp_y = y + dy
            if (temp_x, temp_y) in img.keys():
                check = True
                tot += str(img[(temp_x, temp_y)])
            else:
                tot += '0'
    return int(tot, 2), check


def expand(img, algo_img):
    first_row, first_col = list(img.keys())[0]
    last_row, last_col = list(img.keys())[-1]
    print(first_row, first_col, last_row, last_col)
    new_image = {}
    for r in range(first_row-2, last_row+3):
        for c in range(first_col-2, last_col+3):
            val, check = get_neigh_values(img, r, c)
            if check:
                new_image[(r, c)] = 1 if algo_img[val] == '#' else 0
    return new_image

    

@timer
def solve():
    input = read_file("20")
    algo_img, input_img = process(input)
    N = 2
    print(sum(input_img.values()))
    print('\n')
    for _ in range(N):
        input_img = expand(input_img, algo_img)
        print(sum(input_img.values()))
        print('\n')
    return sum(input_img.values())

result = solve()
print(f'Solution: {result}')