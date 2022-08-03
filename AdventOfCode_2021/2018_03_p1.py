from utils import read_file, timer

@timer
def solve():
    input = read_file("03")
    input = list(zip(*input))
    gamma, epsilon = '', ''
    for position in input:
        gamma_num = max(position, key=position.count)
        gamma += gamma_num
        epsilon += str(1 - int(gamma_num))
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon

result = solve()
print(f'Solution: {result}')