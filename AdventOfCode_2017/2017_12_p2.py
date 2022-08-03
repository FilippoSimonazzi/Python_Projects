from utils import read_file, timer
import networkx as nx

@timer
def solve():
    input = read_file("12")
    graph = nx.Graph()

    for line in input:
        node, neighbors = line.split(' <-> ')
        graph.add_edges_from((node, neighbor) for neighbor in neighbors.split(', '))

    return nx.number_connected_components(graph)

result = solve()
print(f'Solution: {result}')