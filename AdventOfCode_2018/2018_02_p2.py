from utils import read_file, timer

def check_similar(word1, word2):
    tot_diff = 0
    same_letters = ''
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            tot_diff += 1
        else:
            same_letters += word1[i]
        if tot_diff > 1:
            return False
    return same_letters

@timer
def solve():
    input = read_file('02')
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            result = check_similar(input[i], input[j])
            if result:
                return result

result = solve()
print(f'Solution: {result}')