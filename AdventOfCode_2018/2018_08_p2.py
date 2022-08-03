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

    if not len(children):
        return sum(meta)

    return sum(get_value(children[m-1]) for m in meta if m <= len(children))
    

@timer
def solve():
    root = get_tree()
    return get_value(root)


index = -1
input = get_ints(read_file('08'))

result = solve()
print(f'Solution: {result}')