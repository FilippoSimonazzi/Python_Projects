import wget
import os
from collections import defaultdict
import pickle

path_verbi = 'https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/coniugazione_verbi.txt'
path_parole = 'https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/60000_parole_italiane.txt'

verbi = wget.download(path_verbi)
parole = wget.download(path_parole)

with open(f'60000_parole_italiane.txt', 'r') as f:
    parole = f.read().splitlines()
    parole = parole[:-1]

with open(f'coniugazione_verbi.txt', 'r') as f:
    verbi = f.read().splitlines()

words = parole + verbi
words_to_save = defaultdict(list)
for w in words:
    length = len(w)
    starting_letter = w[0]
    if 3 < length <= 10:
        words_to_save[(length, starting_letter)].append(w)

with open(f'italian_words.pkl', 'wb') as f:
    pickle.dump(words_to_save, f)

os.remove(f'coniugazione_verbi.txt')
os.remove(f'60000_parole_italiane.txt')

