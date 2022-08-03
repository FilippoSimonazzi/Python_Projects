from utils import read_file, timer

@timer
def solve():
    input = read_file("15")
    N = 40 * 10**6
    same = 0

    vA = int(input[0].split(' ')[-1])
    vB = int(input[1].split(' ')[-1])
    
    mul_A = 16807
    mul_B = 48271

    for i in range(N):
        vA = (vA * mul_A) % 2147483647
        vB = (vB * mul_B) % 2147483647

        if bin(vA)[-16:] == bin(vB)[-16:]:
            same += 1

    return same


result = solve()
print(f'Solution: {result}')