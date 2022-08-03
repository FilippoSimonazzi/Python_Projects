from utils import read_file, timer

@timer
def solve():
    lengths = read_file("10").split(',')
    lengths = list(map(int, lengths))
    N = 256

    nums = [x for x in range(N)]
    current_pos = 0
    skip_size = 0

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

    return nums[0] * nums[1]

result = solve()
print(f'Solution: {result}')