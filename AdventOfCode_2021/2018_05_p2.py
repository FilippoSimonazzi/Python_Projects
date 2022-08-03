from utils import read_file, timer
from collections import defaultdict

@timer
def solve():
    input = read_file("05")
    start, end = [x.split(' -> ')[0] for x in input], [x.split(' -> ')[1] for x in input]
    start, end = [x.split(',') for x in start], [x.split(',') for x in end]
    
    covered = defaultdict(int)

    for i in range(len(input)):
        x1, y1 = start[i]
        x2, y2 = end[i]
        x1, x2 = int(x1), int(x2)
        y1, y2 = int(y1), int(y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                covered[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                covered[x, y1] += 1
        
        else:
            if x1 < x2 and y1 < y2:
                while x1 <= x2:
                    covered[x1, y1] += 1
                    x1 += 1
                    y1 += 1
            elif x1 > x2 and y1 > y2:
                x1, x2, y1, y2 = x2, x1, y2, y1
                while x1 <= x2:
                    covered[x1, y1] += 1
                    x1 += 1
                    y1 += 1
            elif x1 < x2 and y1 > y2:
                while x1 <= x2:
                    covered[x1, y1] += 1
                    x1 += 1
                    y1 -= 1

            elif x1 > x2 and y1 < y2:
                x1, x2, y1, y2 = x2, x1, y2, y1
                while x1 <= x2:
                    covered[x1, y1] += 1
                    x1 += 1
                    y1 -= 1

    return len(list(covered.values())) - list(covered.values()).count(1)

result = solve()
print(f'Solution: {result}')