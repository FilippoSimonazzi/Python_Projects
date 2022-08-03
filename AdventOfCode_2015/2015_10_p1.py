from utils import read_file, timer

@timer
def solve():
    input = read_file("10")
    n_steps = 1

    input = '111221'

    for _ in range(n_steps):
        i = 0
        new_input = ''
        while i < len(input):
            char = input[i]
            n_char = 1
            if i < len(input): 
                while input[i+1] == input[i]:
                    n_char += 1
                    i += 1
                    if i == len(input) - 1:
                        #new_input += str(n_char) + char
                        break
                    
            new_input += str(n_char) + char
            i += 1
        input = new_input
        
    return input

result = solve()
print(f'Solution: {result}')