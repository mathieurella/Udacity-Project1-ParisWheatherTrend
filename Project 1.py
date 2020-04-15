#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:55:29 2020

@author: mathieurella
"""

import pandas as pd
import matplotlib.pyplot as plt

#CSV Import

Global_Wheather = pd.read_csv('data/Global-Results.csv')
Paris_Wheather = pd.read_csv('data/Paris-Results.csv')

#Rolling Average

    #Paris Rolling Average
pr = pd.DataFrame(Paris_Wheather)
pr['pr10y-ma'] = pr.iloc[:,1].rolling(window=10).mean()

    #Global Rolling Average
gl = pd.DataFrame(Global_Wheather)
gl['gl10y-ma'] = gl.iloc[:,1].rolling(window=10).mean()

# Join both Dataframe
merged_inner = pd.merge(left=gl, right=pr, left_on='year', right_on='year')

merged_inner.rename(columns={'avg_temp_x':'Global_avg_temp',
                             'gl10y-ma':'Global-10y-ma',
                             'avg_temp_y':'Paris_avg_temp',
                             'pr10y-ma':'Paris-10y-ma'},
                             inplace=True)


merged_inner.shape
tp = merged_inner

del tp['Global_avg_temp']
del tp['Paris_avg_temp']

# Graph Line

plt.figure(figsize=[15,10])
tp.plot(x='year')
plt.legend(loc=2)
plt.xlabel('year')
plt.ylabel('Temperature (ºC)')
plt.title('Paris vs Global average temperature (ºC) since 1750')