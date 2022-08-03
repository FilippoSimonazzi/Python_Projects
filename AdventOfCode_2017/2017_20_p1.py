from utils import read_file, timer
from itertools import count


class Particle():
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def update(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def compute_dist(self):
        self.dist = 0
        for i in range(3):
            self.dist += abs(self.p[i])
        

@timer
def solve():
    input = read_file("20")
    particles = []
    distances = []
    # create particles
    for row in input:
        p, v, a = row.split(', ')
        p = list(map(int, p.split('p=<')[1].split('>')[0].split(',')))
        v = list(map(int, v.split('v=<')[1].split('>')[0].split(',')))
        a = list(map(int, a.split('a=<')[1].split('>')[0].split(',')))

        part = Particle(p, v, a)
        particles.append(part)
        part.compute_dist()
        distances.append(part.dist)

    min_dist = min(distances)
    sol_part = [distances.index(min_dist)]

    for it in count(1):
        for i in range(len(particles)):
            part = particles[i]
            part.update()
            part.compute_dist()
            distances[i] = part.dist

        min_dist = min(distances)
        sol_part.append(distances.index(min_dist))
    
        if it > 1000:
            if len(set(sol_part[-1000:])) == 1:
                return sol_part[-1]

        if it > 500000:
            break    


result = solve()
print(f'Solution: {result}')