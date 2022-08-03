from utils import read_file, timer
from collections import Counter, defaultdict
from operator import add

class Scanner:
    def __init__(self, beacons, val, flip):
        self.beacons = beacons
        self.val = val
        self.flip = flip

    def remove_beacon(self, b):
        if any(abs(n) > 1000 for n in b):
            return True
        return False

    def update_beacons(self):
        final_beacons = []
        for b in self.beacons:
            for i in range(3):
                if self.flip[i]:
                    b[i] = -b[i] + self.val[i]
                else:
                    b[i] += self.val[i]
            if not self.remove_beacon(b):
                final_beacons.append(b)
        self.beacons = final_beacons

    
def possibilities(c0, c1):
    out = []
    """for i in range(3):
        if flip[i]:
            c0[i] = -c0[i] + val[i]
        else:
            c0[i] += val[i]"""

    for v0 in c0:
        for v1 in c1:
            n0 = v0 + v1
            n1 = v0 - v1
            out += [n0, n1]
    return out          


def check_poss(c0, c1, pos):
    val = [None] * 3
    flip = [None] * 3
    for n in pos:
        for i in range(3):
            if c1[i] + n == c0[i]:
                val[i] = n
                flip[i] = False
            elif c1[i] - n == c0[i]:
                val[i] = -n
                flip[i] = False
            elif -c1[i] + n == c0[i]:
                val[i] = n
                flip[i] = True
            elif -c1[i] - n == c0[i]:
                val[i] = -n
                flip[i] = True
    return val, flip


def find_dir(s0, s1):
    outs = defaultdict(int)
    for i in range(len(s0.beacons)):
        for j in range(len(s1.beacons)):
            b0 = s0.beacons[i]
            b1 = s1.beacons[j]
            poss = possibilities(b0, b1)
            for ii in range(len(s0.beacons)):
                for jj in range(len(s1.beacons)):
                    b00 = s0.beacons[ii]
                    b11 = s1.beacons[jj]
                    val, flip = check_poss(b00, b11, poss)
                    if all(val):
                        outs[tuple(val)] += 1
                        if outs[tuple(val)] >= 12:
                            return val, flip
    return False, False


@timer
def solve():
    input = read_file("19")
    scanners = []
    for line in input:
        if '---' in line:
            n_beacon = line.split(' ')[-2]
            beacons = []
            if n_beacon == '0':
                val = [0, 0, 0]
                flip = [False, False, False]
            else:
                val = [None, None, None]
                flip = [None, None, None]
        elif line != '':
            beacons.append(list(map(int, line.split(','))))
        else:
            scanners.append(Scanner(beacons, val, flip))
    scanners.append(Scanner(beacons, val, flip))
    
    """s0 = scanners[0]
    i = 1
    while len(scanners) > 1:
        print(i)
        print()
        s1 = scanners[i]
        val, flip = find_dir(s0, s1)
        i += 1
        if val:
            s1.val = val
            s1.flip = flip
            s1.update_beacons()
            s0.beacons += s1.beacons
            scanners.pop(1)
            i = 1
    return len(s0.beacons)"""
    s0, s1 = scanners[0], scanners[1]
    val, flip = find_dir(s0, s1)
    s1.val = val
    s1.flip = flip
    s1.update_beacons()
    s0.beacons += s1.beacons
    scanners.pop(1)
    print(val, flip)

    s4 = scanners[2]
    val, flip = find_dir(s0, s4)

    print(val, flip)

    #print(s0.beacons)

        
result = solve()
print(f'Solution: {result}')