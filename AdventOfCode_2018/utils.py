import time
from re import findall
import requests
import os
import sys

def read_file(name, strip = True):
    with open(f"files/input{name}") as f:
        content = f.readlines()
    
    if strip:
        content = [x.strip() for x in content]
    
    if len(content) == 1:
        return content[0]
    return content


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'\nTime required: {(time.time() - start_time)*1000:.2f} ms\n')
        return result
    return wrapper


def get_ints(string):
    return [int(x) for x in findall(r'\d+', string)]



