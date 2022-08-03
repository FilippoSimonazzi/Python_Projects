from utils import read_file, timer
from operator import xor
from functools import reduce

@timer
def solve():
    lengths = read_file("10")
    lengths = [ord(x) for x in lengths]

    lengths += [17, 31, 73, 47, 23]
    
    N = 256

    N_ROUNDS = 64

    nums = [x for x in range(N)]
    current_pos = 0
    skip_size = 0
    
    for _ in range(N_ROUNDS):
        for l in lengths:
            i = 0
            to_reverse = []
            while i < l:
                to_reverse.append(nums[(current_pos + i) % len(nums)])
                i += 1
            reversed = to_reverse[::-1]

            j = 0
            while j < l:
                nums[(current_pos + j) % len(nums)] = reversed[j]
                j += 1
            
            current_pos = (current_pos + l + skip_size) % len(nums)
            skip_size += 1

    final_hash = []
    for i in range(16):
        part = nums[16*i:16*(i+1)]
        final_hash.append(reduce(xor, part))

    #final_hash = ''.join(list(map(lambda x: x[2:] if len(x) >= 2 else '0'+x, list(map(hex, final_hash)))))
    sol = []
    for el in final_hash:
        hexed = hex(el)[2:]
        if len(hexed) == 1:
            hexed = '0' + hexed
        sol.append(hexed)
    
    return ''.join(sol)

result = solve()
print(f'Solution: {result}')