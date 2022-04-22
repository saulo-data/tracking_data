#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:26:33 2022

@author: https://github.com/saulo-data
"""

#import the libraries
from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the data in order to select the right match
competitions = sb.competitions()
matches = sb.matches(competition_id=43, season_id=3)
lineups = sb.lineups(match_id=8650)
events = sb.events(8650)
passes =events[(events.team=='Brazil') & (events.type=='Pass') & (~events.pass_outcome.isin(['Incomplete', 'Out', 'Unknown', 'Pass Offside']))]

#changing the players full names for the players nicknames
names = {}
for key, value in lineups.items():
    if key == 'Brazil':
        for index, row in value.iterrows():
            names[row['player_name']] = row['player_nickname']

#there is an error at Miranda name
names['João Miranda de Souza Filho'] = 'Miranda'

passes['player'].replace(names, inplace=True)
passes['pass_recipient'].replace(names, inplace=True)

#creating the passes network itself
passes['count'] = 1
passes_network_br = pd.pivot_table(passes, values='count', index='player', 
                                   columns='pass_recipient', aggfunc='sum').fillna(0)

plt.figure(figsize=(10, 10), dpi=100)
plt.style.use('fivethirtyeight')
plt.title('Brazil vs Belgium - World Cup 2018', pad=5)
sns.heatmap(passes_network_br, cmap='Greens', linewidths=.7, linecolor='black',
            cbar=False, annot=True)

plt.show()


#passes_network_br.to_csv('passes_br.csv')

            
    