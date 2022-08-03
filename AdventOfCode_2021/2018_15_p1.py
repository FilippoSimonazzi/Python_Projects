from networkx.algorithms.shortest_paths.generic import shortest_path
from utils import read_file, timer
import numpy as np
import networkx as nx


class Grid:
    def __init__(self, input_file):
        self.map = np.genfromtxt(input_file, delimiter=1, dtype=int)
        self.rows, self.cols = len(self.map), len(self.map[0])

    def create_graph(self):
        self.graph = nx.DiGraph()

        for x in range(self.rows):
            for y in range(self.cols):

                if x < self.rows - 1:
                    self.graph.add_edge((x, y), (x + 1, y),
                                        weight=self.map[x + 1][y])
                    
                    self.graph.add_edge((x + 1, y), (x, y),
                                        weight=self.map[x][y])
                
                if y < self.cols - 1:
                    self.graph.add_edge((x, y), (x, y + 1),
                                        weight=self.map[x][y + 1])
                    
                    self.graph.add_edge((x, y + 1), (x, y),
                                        weight=self.map[x][y])

    def extend_graph(self):
        new_map = self.map.copy()
        for _ in range(4):
            new_map += 1
            new_map[np.where(new_map == 10)] = 1
            self.map = np.concatenate((self.map, new_map), axis=1)
        
        new_map = self.map.copy()
        for _ in range(4):
            new_map += 1
            new_map[np.where(new_map == 10)] = 1
            self.map = np.concatenate((self.map, new_map), axis=0)
            
        self.rows, self.cols = len(self.map), len(self.map[0])

    def get_path_sum(self):
        tot = -self.map[0][0]
        path = nx.shortest_path(self.graph,
                                      source=(0, 0),
                                      target=(self.rows - 1, self.cols - 1),
                                      weight='weight')
        for point in path:
            tot += self.map[point]
        return tot

        
@timer
def solve():
    grid = Grid('./files/input15')
    grid.create_graph()
    return grid.get_path_sum()
    
result = solve()
print(f'Solution: {result}')