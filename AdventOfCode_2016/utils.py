import time
from re import findall
import requests
import os
import sys

def read_file(name, strip=True):
    with open(f"files/input{name}") as f:
        content = f.readlines()
    
    if strip:
        content = [x.strip() for x in content]
    
    if len(content) == 1:
        return content[0]
    return content


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'\nTime required: {(time.time() - start_time)*1000:.2f} ms\n')
        return result
    return wrapper


def get_ints(string):
    return [int(x) for x in findall(r'\d+', string)]


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_orthogonal_neighbours(self):
        adjacent = [
            Point(-1, 0),
            Point(1, 0),
            Point(0, -1),
            Point(0, 1),
        ]
        return [self + n for n in adjacent]

    def get_diagonal_neighbours(self):
        adjacent = [
            Point(-1, -1),
            Point(1, -1),
            Point(-1, 1),
            Point(1, 1),
        ]
        return [self + n for n in adjacent]

    def get_all_neighbours(self):
        return self.get_orthogonal_neighbours() + self.get_diagonal_neighbours()

    def tuple(self):
        return self.x, self.y

    def __call__(self, *args, **kwargs):
        return self.tuple()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __rmul__(self, other: int):
        return Point(other * self.x, other * self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)