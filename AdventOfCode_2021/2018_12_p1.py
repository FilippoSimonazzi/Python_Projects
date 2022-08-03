from os import path
from utils import read_file, timer
from collections import defaultdict


def paths_to_end(start_path, graph):
    tail = start_path[-1]
    # exit case
    if tail == 'end':
        return [start_path]
    paths = []

    # add paths from each cave
    for cave in graph[tail]:
        # cannot revisit lowers
        if cave.islower() and cave in start_path:
            continue
        #print(start_path + [cave])
        paths.extend(paths_to_end(start_path + [cave], graph))
    return paths


@timer
def solve():
    input = read_file("12")
    connections = [line.split('-') for line in input]
    
    # build graph
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)

    # find all paths
    paths = paths_to_end(['start'], graph)
    return len(paths)


result = solve()
print(f'Solution: {result}')