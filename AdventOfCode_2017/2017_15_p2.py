from utils import read_file, timer

@timer
def solve():
    input = read_file("15")
    N = 5 * 10**6
    same = 0
    considered = 0


    vA = int(input[0].split(' ')[-1])
    vB = int(input[1].split(' ')[-1])

    if vA % 4 == 0:
        values_A = [vA]
    else:
        values_A = []
    if vB % 8 == 0:
        values_B = [vB]
    else:
        values_B = []
    
    #vA = 65
    #vB = 8921

    mul_A = 16807
    mul_B = 48271

    while considered < N:
        if len(values_A) > 0 and len(values_B) > 0:
            considered += 1
            if bin(values_A[0])[-16:] == bin(values_B[0])[-16:]:
                same += 1
            
            if considered % 10 ** 5 == 0:
                print(considered)
            del values_A[0]
            del values_B[0]
        vA = (vA * mul_A) % 2147483647
        vB = (vB * mul_B) % 2147483647

        if vA % 4 == 0:
            values_A.append(vA)
        if vB % 8 == 0:
            values_B.append(vB)

    return same


result = solve()
print(f'Solution: {result}')