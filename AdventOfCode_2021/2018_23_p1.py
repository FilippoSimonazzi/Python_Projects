from utils import read_file, timer
import dataclasses, functools, re
from typing import Optional

@dataclasses.dataclass
class Node:
    can_stop: bool = True
    room: Optional[str] = None

    @property
    def hallway(self) -> bool:
        return self.room is None

room_map = {id: 'ABDC'[i%4] for i, id in enumerate('abcdefghijklmnopqrs')}
make_space = lambda id: Node(can_stop=id not in 'cegi', room=room_map.get(id))

# abcdefghijk
#   l n p r
#   m o q s

costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
edges = {
    'a': 'b', 'b': 'ac', 'c': 'bdl', 'd': 'ce', 'e': 'dfn', 'f': 'eg',
    'g': 'fhp', 'h': 'gi', 'i': 'hjr', 'j': 'ik', 'k': 'j', 'l': 'cm',
    'n': 'eo', 'p': 'gq', 'r': 'is', 'm': 'l', 'o': 'n', 'q': 'p', 's': 'r',
}

rooms = {'A': 'lm', 'B': 'no', 'C': 'pq', 'D': 'rs'}
spaces = {id: make_space(id) for id in 'abcdefghijklmnopqrs'}

def room_ready(state, kind):
    return all(state.get(id) in (None, kind) for id in rooms[kind])