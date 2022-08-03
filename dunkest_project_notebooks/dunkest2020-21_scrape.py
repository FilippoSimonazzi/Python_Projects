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
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

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
    
 
def construct_url(week, rounds):
    season_id = 5
    season = '2020-2021'
    base_url = f'https://www.dunkest.com/en/nba/stats/players/table/regular-season/{season}?season_id={season_id}&mode=dunkest&stats_type=avg&weeks[]={week}'
    rounds_url = ''.join([f'&rounds[]={i}' for i in range(1, rounds+1)])
    teams_url = ''.join([f'&teams[]={i}' for i in range(1, 31)])
    positions_url = ''.join([f'&positions[]={i}' for i in range(1, 4)])
    end_url = '&player_search=&min_cr=4&max_cr=30&sort_by=player&sort_order=desc&iframe=yes'
    return base_url + rounds_url + teams_url + positions_url + end_url
    
    
def scrape_dunkest_table(week):
    if not os.path.exists(f'{DATA_DIR}/Credits/2020-21'):
        os.makedirs(f'{DATA_DIR}/Credits/2020-21')
    df = pd.read_csv(f'{DATA_DIR}/Credits/RoundsPerWeek2020-21.csv')
    season = '2020-2021'
    rounds = df.loc[week]['n_rounds']
    
    headers = ['POS', 'TEAM', 'PDK', 'CR', 'PLUS', 
               'GP', 'MIN', 'ST', 'PTS', 'REB', 'AST', 'STL',
               'BLK', 'BA', 'FGM', 'FGA', 'FG_perc', '3PM', 
               '3PA', '3P%', 'FTM', 'FTA', 'FT_perc', 'OREB', 
               'DREB', 'TOV', 'PF', '+/-']
    
    positions = ['G', 'F', 'C']
    
    ser = Service('/home/filipo/Downloads/geckodriver-v0.30.0-linux32/geckodriver')
    op = webdriver.FirefoxOptions()
    op.headless = True
    driver = webdriver.Firefox(service=ser, options=op)
    url = construct_url(week, rounds)
    driver.get(url)
    time.sleep(SLEEP_TIME)
    
    data = {}
    
    button = driver.find_elements('css selector', 'li')
    button = [b for b in button if len(b.text) > 0]
    n_pages = int(button[-2].text)
    
    for _ in range(n_pages):
        table = driver.find_element('id', 'statsTableBody')
        lines = table.find_elements('css selector', 'tr')
        text_lines = [line.text.split(' ') for line in lines]
    
        for line in lines:
            text_line = line.text.split(' ')
            for i, el in enumerate(text_line):
                if el in ['G', 'F', 'C']:
                    starting_idx = i
                    break
            
            player_url = line.find_elements('css selector', 'td')[0].find_elements('tag name', 'a')[0].get_attribute('href')
            soup = BeautifulSoup(urlopen(player_url), 'lxml')
            firstname = soup.find('span', {'class': 'player-info__firstname'}).text.strip()
            lastname = soup.find('span', {'class': 'player-info__lastname'}).text.strip()
            name = ' '.join([firstname, lastname])
            
            data[name] = {}
            for i in range(starting_idx, len(text_line)):
                data[name][headers[i-starting_idx]] = text_line[i]
        
        button = driver.find_elements('css selector', 'li')
        button = [b for b in button if len(b.text) > 0]
        button[-1].click()

    df = pd.DataFrame.from_dict(data, columns=headers, orient='index')
    df['WEEK'] = week
    df.reset_index(inplace=True)
    df.rename({'index': 'NAME'}, axis=1, inplace=True)
    df.to_csv(f'{DATA_DIR}/Credits/2020-21/Week_{week}.csv', index_label=False)
    driver.close()
    
#for week in range(1, 60):
for week in range(30, 60):
    scrape_dunkest_table(week)
    print(f'Week {week} scraped successfully!')
