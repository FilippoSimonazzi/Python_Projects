from utils import read_file, timer

def output_pixel(image, pos, space, algo):
    i, j = pos
    res = ''
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            ni, nj = i + di, j + dj
            if ni not in range(len(image)) or nj not in range(len(image[0])): 
                res += space
            else:
                res += image[ni][nj]
    idx = int(res, 2)
    return algo[idx]


def get_output(image, algo_img, space = '0'):
    count = 0
    new_image = []
    
    for i in range(-1, len(image) + 1):
        row = ''
        for j in range(-1, len(image[0]) + 1):
            pixel = output_pixel(image, (i, j), space, algo_img)
            if pixel == '1': count += 1
            row += pixel
        new_image.append(row)
    space = output_pixel(image, (-2, -2), space, algo_img)
    return new_image, count, space


def process(data):
    divide = data.index('')
    algo_img = ''.join(data[:divide])
    algo_img = ['1' if x=='#' else '0' for x in algo_img]
    input_img = data[divide+1:]
    input_img = [['1' if x=='#' else '0' for x in row] for row in input_img]
    return algo_img, input_img

@timer
def solve():
    input = read_file("20")
    algo_img, input_img = process(input)
    space = '0'

    for i in range(50):
        input_img, count, space = get_output(input_img, algo_img, space)
        print(i, count)

result = solve()
print(f'Solution: ')