import os
import time
from dateutil import parser
from collections import defaultdict

import numpy as np
import pandas as pd
import math


# utility functions
def normal_round(n, decimals=0):
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals
    

def PTS(row):
    return row['PTS']

def DRB(row):
    return row['DRB']

def ORB(row):
    return row['ORB'] * 1.25

def AST(row):
    return row['AST'] * 1.5

def STL(row):
    return row['STL'] * 1.5

def TOV(row):
    return row['TOV'] * -1.5

def BLK(row):
    return row['BLK'] * 1.5

def BA(row):
    return row['BA'] * -0.5

def DD(row):
    categories = row[['PTS', 'TRB', 'AST', 'STL', 'BLK']].values
    tot = 0
    for stat in categories:
        if len(str(stat)) >= 2:
            tot += 1
    return 5 if tot >= 2 else 0

def TD(row):
    categories = row[['PTS', 'TRB', 'AST', 'STL', 'BLK']].values
    tot = 0
    for stat in categories:
        if len(str(stat)) >= 2:
            tot += 1
    return 10 if tot >= 3 else 0

def QD(row):
    categories = row[['PTS', 'TRB', 'AST', 'STL', 'BLK']].values
    tot = 0
    for stat in categories:
        if len(str(stat)) >= 2:
            tot += 1
    return 50 if tot >= 4 else 0

def ST(row):
    return row['ST']


def ThreePT(row):
    made = row['3P']
    if made < 3:
        return 0
    elif made >= 5:
        return 5
    return made

def WIN(row):
    categories = row[['TEAM', 'W']].values
    if len(set(categories)) == 1:
        return 3
    else:
        return -3

def MissedShot(row):
    return -(row['FGA'] - row['FG'])

def MissedFT(row):
    return -(row['FTA'] - row['FT'])

def FouledOut(row):
    if row['PF'] >= 6:
        return -5
    return 0


# Scoring system
PLAYER_SCORE = {
    'PTS': PTS,
    'DRB': DRB,
    'ORB': ORB,
    'AST': AST,
    'STL': STL,
    'TOV': TOV,
    'BLK': BLK,
    'BA': BA,
    'DD': DD,
    'TD': TD,
    'QD': QD,
    'ST': ST,
    'ThreePT': ThreePT,
    'WIN': WIN,
    'MissedShot': MissedShot,
    'MissedFT': MissedFT,
    'FouledOut': FouledOut,
}
