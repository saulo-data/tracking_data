#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:03:57 2022

@author: saulo
"""

#libraries
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import VerticalPitch
import json

#loading and preparing the data
with open('match_360_1.JSON', 'rb') as f:
    match_360 = json.load(f)
    
match_freeze = match_360[5]['freeze_frame']

x = []
y = []
actor = []
team = []
for z in match_freeze:
    x.append(z['location'][0])
    y.append(z['location'][1])
    actor.append(z['actor'])
    team.append(z['teammate'])
    

#dataframe
df = pd.DataFrame({'x': x, 
                   'y': y, 
                   'actor': actor, 
                   'team': team})

#plotting the pitch
fig, ax = plt.subplots(figsize=(6, 10))
pitch = VerticalPitch(pitch_type='statsbomb', half=True, pitch_color='white', 
                      line_color='black')

pitch.draw(ax=ax)

# #plotting the polygons on the pitch
team1,team2 = pitch.voronoi(df.x,df.y,df.team)
pitch.scatter(df.x, df.y, ax=ax, c=df.team)
t1 = pitch.polygon(team1, ax=ax, fc='gray', ec='black', lw=3, alpha=0.25)
t2 = pitch.polygon(team2, ax=ax, fc='black', ec='black', lw=3, alpha=0.25)



