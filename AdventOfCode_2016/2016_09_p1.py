from utils import read_file, timer

@timer
def solve():
    input = read_file("09")
    
    out = ''
    pos = 0
    while pos < len(input):
        letter = input[pos]
        if letter.isalpha():
            out += letter
            pos += 1
        else:
            pos += 1
            next_letter = input[pos]
            length = next_letter
            while next_letter != 'x':
                pos += 1
                next_letter = input[pos]
                if next_letter != 'x':
                    length += next_letter
            length = int(length)
            pos += 1
            next_letter = input[pos]
            rep = next_letter
            while next_letter != ')':
                pos += 1
                next_letter = input[pos]
                if next_letter != ')':
                    rep += next_letter
            rep = int(rep)
            pos += 1
            
            to_repeat = input[pos:pos+length]
            for _ in range(rep):
                out += to_repeat
            pos += length
    return len(out)

result = solve()
print(f'Solution: {result}')