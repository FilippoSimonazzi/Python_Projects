import os
import time
from tqdm import notebook
from collections import defaultdict
from datetime import datetime
from dateutil import parser
import sys

import pandas as pd
import numpy as np
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

from constants import DATA_DIR, SEASONS

SLEEP_TIME = 1

NAMES_CONVERSION = {'ć': 'c', 'č': 'c', 'Č': 'C', 'ç': 'c',
                    'ã': 'a', 'ā': 'a', 'á': 'a', 'ä': 'a', 'Á': 'A',
                    'ž': 'z',
                    'í': 'i', 'İ': 'I', 'ï': 'i', 'ı': 'i',
                    'ö': 'o', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'Ó': 'O', 'Ö': 'O',
                    'é': 'e', 'ê': 'e', 'ë': 'e', 'è': 'e',
                    'Š': 'S', 'ș': 's', 'š': 's', 'ş': 's',
                    'ū': 'u', 'ü': 'u', 'ú': 'u',
                    'ņ': 'n', 'ń': 'n',
                    'ģ': 'g', 'ğ': 'g',
                    'ý': 'y',
                    'Ž': 'Z',
                    'ř': 'r'}
                    
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    
    
def get_boxscores(season, start_date, end_date):
    if not os.path.exists(f'{DATA_DIR}/Boxscores'):
        os.makedirs(f'{DATA_DIR}/Boxscores')
    if not os.path.exists(f'{DATA_DIR}/Boxscores/{season}'):
        os.makedirs(f'{DATA_DIR}/Boxscores/{season}')
                    
    url_boxscore = f'https://www.basketball-reference.com/boxscores/'
    
    date_list = [d.strftime('%Y-%m-%d') for d in pd.date_range(start_date, end_date)]
    
    print(f'Scraping boxscores for the season {season}...')
    
    for date in notebook.tqdm(date_list):
        year, month, day = date.split('-')
        url = f'{url_boxscore}?month={month}&day={day}&year={year}'
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        games = soup.find_all('div',class_='game_summary expanded nohover')
        
        for game in games:
            summary = {}
            
            host = game.find_all('table')[1].find_all('a')[1]['href'][7:10]
            
            # check if dataset already exists
            if os.path.exists(f'{DATA_DIR}/Boxscores/{season}/' + date + '_' + host + '.csv'):
                continue

            winner = game.find_all('tr', class_='winner')[0].find_all('td')
            loser = game.find_all('tr', class_='loser')[0].find_all('td')
            
            summary['winner'] = [winner[0].find('a')['href'][7:10], int(winner[1].text)]
            summary['loser'] = [loser[0].find('a')['href'][7:10], int(loser[1].text)]

            url_game = url_boxscore + game.find('a', text='Box Score')['href'][11:]
            html_game = urlopen(url_game)
            soup_game = BeautifulSoup(html_game, 'lxml')
            
            tables = soup_game.find_all('table', limit=4)[2:]
            column_headers = ['NAME','DATE','TEAM','HOME','W','W_PTS','L','L_PTS','MP','FG','FGA','FG_perc','3P','3PA','3P_perc','FT','FTA',
                              'FT_perc','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS','+/-','TS_perc','eFG_perc','3PAr',
                              'FTr','ORB_perc','DRB_perc','TRB_perc','AST_perc','STL_perc','BLK_perc','TOV_perc','USG_perc','ORtg','DRtg','BPM', 'ST']
            
            # --------
            # get shots blocked from play-to-play
            url_pbp = url_boxscore + 'pbp/' + game.find('a', text='Box Score')['href'][11:]
            html_pbp = urlopen(url_pbp)
            soup_pbp = BeautifulSoup(html_pbp, 'lxml')
            
            table_shots_blocked = soup_pbp.find_all('table', {'id': 'pbp'})[0].find_all('tr')
            shots_blocked = []
            for t in table_shots_blocked:
                if 'block' in t.get_text():
                    shots_blocked.append(t.get_text().strip().split('\n')[1].split('(')[0])
            
            shots_blocked = [shot.replace('\xa0', '').replace('-', '') for shot in shots_blocked]
            shots_blocked = [' '.join(''.join(filter(lambda c: not c.isdigit(), shot)).split(' ')[:2]) for shot in shots_blocked]
            # --------

            for team in ['winner', 'loser']:
                basic_stat_template = f'box-{summary[team][0].upper()}-game-basic'
                advanced_stat_template = f'box-{summary[team][0].upper()}-game-advanced'
                if summary[team][0] == host:
                    home = 1
                else:
                    home = 0
                
                data_basic = soup_game.find('table', id=basic_stat_template).find('tbody').find_all('tr', class_=None)
                data_advanced = soup_game.find('table', id=advanced_stat_template).find_all('tr', class_=None)[1:]
                game_data = [date, summary[team][0], home, 
                             summary['winner'][0], summary['winner'][1],
                             summary['loser'][0], summary['loser'][1]]
                
                n = len(data_basic)
                
                player_names = [data_basic[i].find('a').get_text() for i in range(n)]
                player_data = []
                                                
                for i in range(n):
                    if data_basic[i].find('td').get_text() not in ['Did Not Play', 'Not With Team']:
                        data = [player_names[i]] + game_data + \
                               [td.get_text() for td in data_basic[i].find_all('td')] + \
                               [td.get_text() for td in data_advanced[i].find_all('td')[1:]] + \
                               [int(1) if i <= 4 else int(0)]
                        player_data.append(data)
                
                df = pd.DataFrame(player_data, columns=column_headers).fillna(0)
                df.loc[:,'FG':'BPM'] = df.loc[:,'FG':'BPM'].apply(pd.to_numeric)  
                
                df['BA'] = None
                
                # --- Add BA ---
                for i in range(len(player_data)):
                    name_for_BA = player_data[i][0].split(' ')[0][0] + '. ' + player_data[i][0].split(' ')[1]
                    blocks_against = shots_blocked.count(name_for_BA)
                    idx = df.loc[df.NAME==player_data[i][0]].index.values[0]
                    df.at[idx, 'BA'] = blocks_against
                # -------------
                
                df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
                
                df.to_csv(f'{DATA_DIR}/Boxscores/{season}/' + date + '_' + summary[team][0] +'.csv', index=False)
                time.sleep(SLEEP_TIME)
            time.sleep(SLEEP_TIME)
    return None


def scrape_season(season):
    df = pd.read_csv(f'{DATA_DIR}/SeasonsInfo.csv')
    start_date, end_date = df.loc[season]['RS_START'], df.loc[season]['RS_END']
    return get_boxscores(season, start_date, end_date)
    

def check_regular_season_download(season):
    _, _, games = next(os.walk(f'{DATA_DIR}/Boxscores/{season}'))
    df = pd.read_csv(f'{DATA_DIR}/SeasonsInfo.csv')
    n_games = eval(df.loc[season]['N_GAMES'])
    
    teams = set()
    check_calendar = []
    calendar = defaultdict(list)
    for game in games:
        team = game[-7:-4]
        teams.add(team)
        calendar[team].append(datetime.strptime(game[:-8], '%Y-%m-%d').date())

    for key in calendar.keys():
        calendar[key] = sorted(calendar[key])
        calendar[key] = [f'{x.day}-{x.month}-{x.year}' for x in calendar[key]]
        if len(calendar[key]) in n_games:
            check_calendar.append([key, True])
        else:
            check_calendar.append([key, False])

    is_valid = all([item[1] for item in check_calendar])
    
    if 'TEAMS' not in df.columns:
        df['TEAMS'] = [None] * df.shape[0]
    df.at[season, 'TEAMS'] = list(teams)
    
    if is_valid:
        df.to_csv(f'{DATA_DIR}/SeasonsInfo.csv', index_label=False)
        return True
    else:
        print(f"There are issues with season {season}... Dataset not created!\n")
        return False
    

def merge_boxscores(season):
    try:
        _, _, games = next(os.walk(f'{DATA_DIR}/Boxscores/{season}'))
    except StopIteration:
        print(f"Folder not found for season {season}... Check if dataset already exists or if boxscores havent't been downloaded yet!\n")
        return None
    
    if not check_regular_season_download(season):
        return None
    
    df = pd.read_csv(f'{DATA_DIR}/Boxscores/{season}/{games[0]}')
    os.remove(f'{DATA_DIR}/Boxscores/{season}/{games[0]}')
    
    for game in games[1:]:
        temp = pd.read_csv(f'{DATA_DIR}/Boxscores/{season}/{game}')
        df = df.append(temp)
        df.reset_index(drop=True, inplace=True)
        os.remove(f'{DATA_DIR}/Boxscores/{season}/{game}')
        
    os.rmdir(f'{DATA_DIR}/Boxscores/{season}')
    df.to_csv(f'{DATA_DIR}/Boxscores/{season}.csv', index_label=False)
    print(f'Dataset for season {season} created!\n')
    
 
def fix_name(name):
    new_name = ''
    for char in name:
        if char in NAMES_CONVERSION:
            new_name += NAMES_CONVERSION[char]
        else:
            new_name += char
    return new_name


def fix_name_df(season):
    df = pd.read_csv(f'{DATA_DIR}/Boxscores/{season}.csv')
    df['NAME'] = df['NAME'].apply(fix_name)
    df.to_csv(f'{DATA_DIR}/Boxscores/{season}.csv', index_label=False)
    return df
    
  
season_idx = int(sys.argv[1])
season = SEASONS[season_idx]

scrape_season(season)
#merge_boxscores(season)
#fix_name_df(season)
print(f'Season {season} scraped successfully!')
