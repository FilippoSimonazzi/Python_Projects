from collections import defaultdict
import pickle
import networkx as nx
import enchant
import time
from tqdm import tqdm

max_length = int(input('Insert maximum word length: '))
depths = [x for x in range(3, max_length+1)]
starting_positions = [x for x in range(25)]

with open('italian_words.pkl', 'rb') as f:
    italian_words = pickle.load(f)

# --- create graph ---

# 1) get letters and create nodes
def get_letters():
    letters = []
    it = 0
    while len(letters) < 25:
        l = input(f'Insert letter {it+1}: ').lower()
        while not (l.isalpha() and len(l)==1 or l=='qu' or l=='in'):
            print(f'{l} is not a valid input.')
            l = input('Insert next letter: ').lower()
        letters.append(l)
        it += 1
    return letters

def addNodes(G):
    letters = get_letters()
    for idx, l in enumerate(letters):
        G.add_node(idx, letter=l)
    return G

# 2) create edges
def neighbours(x, y, mapping, grid):
    v = grid[(x, y)]
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not i == j == 0:
                if (x+i, y+j) in grid.keys():
                    mapping[v].append(grid[(x+i, y+j)])
    return mapping

def create_mapping():
    positions = [[x+i for x in range(5)] for i in range(0, 21, 5)]
    grid = {(x, y): i for x, r in enumerate(positions) for y, i in enumerate(r)}
    mapping = defaultdict(list)
    for x in range(5):
        for y in range(5):
            mapping = neighbours(x, y, mapping, grid)
    return mapping

def addEdges(G):
    mapping = create_mapping()
    for key, value in mapping.items():
        for v in value:
            G.add_edge(key, v)
    return G

# 3) Create graph
def create_graph():
    G = nx.Graph()
    G = addNodes(G)
    G = addEdges(G)
    return G

# --- find all possible paths ---

# 1) Find paths given starting node 'u' and depth 'n',
#    resulting in a word of length n+1.
def findPaths(G, u, n):
    if n == 0:
        return [[u]]
    paths = [[u] + path for neighbor in G.neighbors(u) for path in findPaths(G, neighbor, n-1) if u not in path]
    return paths

# 2) Find paths for each starting position and each depth
def findAllPaths(G):
    paths = defaultdict(list)
    print('Finding all paths...')
    for n in tqdm(depths):
        start = time.time()
        for u in starting_positions:
            paths[n+1].append(findPaths(G, u, n))
        end = time.time()
    print()
    return paths

# 3) create words from the paths
def readPaths(paths, G):
    outPaths = defaultdict(list)
    findLetter = lambda u: G.nodes[u]['letter']
    print('Reading paths...')
    for n in tqdm(depths):
        start = time.time()
        letterPaths = []
        temp_paths = paths[n+1]
        for path in temp_paths:
            for p in path:
                letterPaths.append(''.join([findLetter(u) for u in p]))
        outPaths[n+1] = letterPaths
        end = time.time()
    print()
    return outPaths

# 4) Find all words
def findWords(G):
    paths = findAllPaths(G)
    words = readPaths(paths, G)
    return words

# --- Get valid words ---
def check_words_enchant(words):
    dictionary = enchant.Dict('it_IT')
    valid_words = defaultdict(list)
    seenWords = set()
    points = {4: 1, 5: 2, 6: 3, 7: 5, 8: 11, 9: 11, 10: 11}
    tot = 0
    print('Check valid words...')
    for n in tqdm(depths):
        start = time.time()
        temp_words = words[n+1]
        for word in temp_words:
            if dictionary.check(word):
                if word not in seenWords:
                    valid_words[len(word)].append(word)
                    tot += points[len(word)]
                seenWords.add(word)
        end = time.time()
    return valid_words, tot

# --- Get valid words ---
def check_words_italian_words(words):
    valid_words = defaultdict(list)
    seenWords = set()
    points = {4: 1, 5: 2, 6: 3, 7: 5, 8: 11, 9: 11, 10: 11}
    tot = 0
    print('Check valid words...')
    for n in tqdm(depths):
        start = time.time()
        temp_words = words[n+1]
        for word in temp_words:
            if word not in seenWords:
                starting_letter = word[0]
                if word in italian_words[(n+1, starting_letter)]:
                    valid_words[len(word)].append(word)
                    tot += points[len(word)]
            seenWords.add(word)
        end = time.time()
    return valid_words, tot

