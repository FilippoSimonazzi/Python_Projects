from utils import read_file, timer
from itertools import count
from collections import Counter


class Particle():
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def update(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]
        
def handle_collision(particles, distances):
    # handle collision
    collision = Counter(distances)

    pos_to_remove = []
    for k, v in collision.items():
        if v > 1:
            pos_to_remove.append(k)
    
    idx_to_remove = []
    for idx in range(len(distances)):
        if distances[idx] in pos_to_remove:
            idx_to_remove.append(idx)

    distances = [d for idx, d in enumerate(distances) if idx not in idx_to_remove]
    particles = [p for idx, p in enumerate(particles) if idx not in idx_to_remove]

    tot_collison = len(idx_to_remove)
    return particles, distances, tot_collison


@timer
def solve():
    input = read_file("20")
    particles = []
    distances = []  
    collisions = []
    # create particles
    for row in input:
        p, v, a = row.split(', ')
        p = list(map(int, p.split('p=<')[1].split('>')[0].split(',')))
        v = list(map(int, v.split('v=<')[1].split('>')[0].split(',')))
        a = list(map(int, a.split('a=<')[1].split('>')[0].split(',')))

        part = Particle(p, v, a)
        particles.append(part)
        distances.append(tuple(part.p))

    particles, distances, tot_collision = handle_collision(particles, distances)
    collisions.append(tot_collision)

    for it in count(1):
        for i in range(len(particles)):
            part = particles[i]
            part.update()
            distances[i] = tuple(part.p)
    
        particles, distances, tot_collision = handle_collision(particles, distances)
        collisions.append(tot_collision)
        
        if it > 1000:
            if set(collisions[-1000:]) == {0}:
                return len(particles)

        if it > 500000:
            print('interrupt before check')
            return None


result = solve()
print(f'Solution: {result}')