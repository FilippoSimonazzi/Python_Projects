from utils import read_file, timer, Point

real = read_file("13")

dots, folds = set(), []
def parse(input):
    divide = input.index('')
    points, folds = input[:divide], input[divide + 1:]

    dots = set(tuple(map(int, p.split(','))) for p in points)
    folds = [f.split(' ')[-1].split('=') for f in folds]
    folds = [(0, int(f[1])) if f[0] == 'x' else (1, int(f[1])) for f in folds]

    return dots, folds

def fold(direction, value):
    for dot in dots.copy():
        if dot[direction] > value:
            d = list(dot)
            d[direction] = 2 * value - d[direction]
            dots.remove(dot)
            dots.add(tuple(d))

def print_dots():
    xmax, ymax = map(max, zip(*dots))
    for y in range(ymax+1):
        for x in range(xmax+1):
            print("#" if (x, y) in dots else ".", end=" ")
        print()

dots, folds = parse(real)
fold(*folds[0])
print(f"Puzzle 1: {len(dots)}")
for f in folds[1:]:
    fold(*f)
print_dots()