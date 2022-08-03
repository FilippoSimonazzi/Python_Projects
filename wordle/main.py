from nltk.corpus import words
import nltk
import random
from colorama import init
from termcolor import colored
import os
init()

try:
    words = set(words.words())
except:
    nltk.download('words')
    words = set(words.words())
    os.system('cls' if os.name=='nt' else 'clear')
    
words = [w for w in words if len(w) == 5]

def get_word():    
    N = len(words) - 1
    idx = random.randint(0, N)
    return words[idx].upper()

def get_user_word(precise, in_word, old_guess):
    guess = input('Insert word: ')
    while len(guess) != 5:
        os.system('cls' if os.name=='nt' else 'clear')
        if precise is not None:        
            print_output(precise, in_word, old_guess)
        print('Your word must have 5 letters!\n')
        guess = input('Insert word: ')
    while not all([l.isalpha() for l in guess]):
        os.system('cls' if os.name=='nt' else 'clear')
        if precise is not None:
            print_output(precise, in_word, old_guess)
        print('Your word must contain only letters!\n')
        guess = input('Insert word: ')
    if guess.lower() == 'proud':
        return 'PROUD'
    while not guess.lower() in words:
        os.system('cls' if os.name=='nt' else 'clear')
        if precise is not None:
            print_output(precise, in_word, old_guess)
        print('Your word must be an english word!\n')
        guess = input('Insert word: ')
        if guess.lower() == 'proud':
            os.system('cls' if os.name=='nt' else 'clear')
            return 'PROUD'
    os.system('cls' if os.name=='nt' else 'clear')
    return guess.upper()

def check_guess(word, guess):
    precise_out = [False] * 5
    in_word = [False] * 5
    for i in range(5):
        if word[i] == guess[i]:
            precise_out[i] = True
        if guess[i] in set(word):
            in_word[i] = True
    return precise_out, in_word

def print_output(precise_out, in_word, guess):
    to_print = []
    for i in range(5):
        if precise_out[i]:
            to_print.append((guess[i], 'green'))
        elif in_word[i]:
            to_print.append((guess[i], 'yellow'))
        else:
            to_print.append((guess[i], 'white'))
    print(colored(to_print[0][0], to_print[0][1]) + '  ' + \
            colored(to_print[1][0], to_print[1][1]) + '  ' + \
            colored(to_print[2][0], to_print[2][1]) + '  ' +\
            colored(to_print[3][0], to_print[3][1]) + '  ' + \
            colored(to_print[4][0], to_print[4][1]) + '\n')


def print_correct_result(to_print):
    print(colored(to_print[0], 'red') + '  ' + \
            colored(to_print[1], 'red') + '  ' + \
            colored(to_print[2], 'red') + '  ' +\
            colored(to_print[3], 'red') + '  ' + \
            colored(to_print[4], 'red') + '\n')
def main():
    word = get_word()
    word = 'HELLO'
    guess = get_user_word(precise=None, in_word=None, old_guess=None)
    all_guesses = []
    it = 1
    while it < 6 and word != guess:
        precise, in_word = check_guess(word, guess)
        all_guesses.append((precise, in_word, guess))
        for data in all_guesses:
            print_output(data[0], data[1], data[2])
        
        
        guess = get_user_word(precise, in_word, guess)
        it += 1

    precise, in_word = check_guess(word, guess)
    all_guesses.append((precise, in_word, guess))
    for data in all_guesses:
        print_output(data[0], data[1], data[2])
    
    if word != guess:
        print_correct_result(word)

main()
