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


def paths_with_single_revisit(start_path, graph, can_revisit_small=True):
    tail = start_path[-1]
    if tail == 'end':
        return [start_path]
    paths = []
    for cave in graph[tail]:
        # can't revisit start
        if cave == 'start':
            continue
        # can only visit one small cave twice
        # if we've already been to this small cave
        if cave.islower() and cave in start_path:
            if can_revisit_small:
                # add paths where the small cave is revisited
                paths.extend(
                    paths_with_single_revisit(start_path + [cave], graph, False)
                )
        else:
            paths.extend(
                paths_with_single_revisit(start_path + [cave], graph, can_revisit_small)
            )
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
    paths = paths_with_single_revisit(['start'], graph)
    return len(paths)


result = solve()
print(f'Solution: {result}')