from utils import read_file, timer

@timer
def solve():
    input = read_file("19")
    
    input = ['H => HO', 'H => OH', 'O => HH']
    replacements = {}
    for row in input:
        start, end = row.split(' => ')
        if start not in replacements.keys():
            replacements[start] = [end]
        else:
            replacements[start].append(end)
    
    word = 'HOH'
    list_word = list(word)
    new_words = set()
    for i in range(len(list_word)):
        temp_word = list_word.copy()
        letter = temp_word[i]
        
        

result = solve()
print(f'Solution: ')