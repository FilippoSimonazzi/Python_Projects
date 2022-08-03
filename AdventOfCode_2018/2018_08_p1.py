from utils import read_file, timer, get_ints

def get_tree():
    global index, input

    nc = input[(index := index + 1)]
    nm = input[(index := index + 1)]

    children = [get_tree() for _ in range(nc)]
    meta = [input[(index := index + 1)] for _ in range(nm)]

    return (children, meta)


def get_value(tree):
    children, meta = tree
    return sum(get_value(child) for child in children) + sum(meta)
    

@timer
def solve():
    root = get_tree()
    return get_value(root)


index = -1
input = get_ints(read_file('08'))

result = solve()
print(f'Solution: {result}')