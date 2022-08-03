import collections
import time
from utils import check_words_italian_words, create_graph, findWords
import pandas as pd
from tabulate import tabulate

start = time.time()
G = create_graph()
words = findWords(G)
valid_words, tot = check_words_italian_words(words)
end = time.time()
print(f'Total time italian words: {round(end-start, 3)} s. Tot: {tot}')

for key in valid_words.keys():
    df = pd.DataFrame.from_dict(sorted(valid_words[key]))
    print(tabulate(df, headers='keys', tablefmt='psql'))