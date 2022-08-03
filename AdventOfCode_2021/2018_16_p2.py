from utils import read_file, timer
from math import prod



def from_hex_to_bin(hex, scale=16, n_bits=4):
    return bin(int(hex, scale))[2:].zfill(n_bits)

lookup = {str(x): from_hex_to_bin(str(x)) for x in [el for el in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']}

def read_hex_in_bin(hex):
    out = ''
    for chr in hex:
        out += lookup[chr]
    return out

def convert_dec(binary):
    return int(binary, 2)

def operation(type_id, vals):
    if type_id == 0:
        return sum(vals)
    elif type_id == 1:
        return prod(vals)
    elif type_id == 2:
        return min(vals)
    elif type_id == 3:
        return max(vals)
    elif type_id == 5:
        if vals[1] < vals[0]:
            return 1
        return 0
    elif type_id == 6:
        if vals[1] > vals[0]:
            return 1
        return 0
    elif type_id == 7:
        if vals[1] == vals[0]:
            return 1
        return 0



def read_package(data, n=0, versions=[]):
    versions.append(convert_dec(data[n:n+3]))
    type_id = convert_dec(data[n+3:n+6])
    pid = data[n+6]

    if type_id == 4:
        out = ''
        idx = n + 6
        while data[idx] == '1':
            out += data[idx+1:idx+5]
            idx += 5
        out += data[idx+1:idx+5]
        idx += 5
        out = convert_dec(out)
        return idx, out, versions
    
    else:
        vals = []
        if pid == '0':
            start = n + 22
            lenght = convert_dec(data[n+7:start])
            end = start + lenght
            while start < end:
                start, s, versions = read_package(data, start, versions)
                vals.append(s)
            return start, operation(type_id, vals), versions

        else:
            num = convert_dec(data[n+7:n+18])
            start = n + 18
            for _ in range(num):
                start, s, versions = read_package(data, start, versions)
                vals.append(s)
            return start, operation(type_id, vals), versions

@timer
def solve():
    input = read_file("16")
    data = read_hex_in_bin(input)
    
    _, vals, _ = read_package(data)
    
    return vals

result = solve()
print(f'Solution: {result}')