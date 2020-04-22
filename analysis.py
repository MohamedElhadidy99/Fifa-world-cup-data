# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 05:08:21 2020

@author: Mohamed
"""
'''World cup data from 1930 to 2014'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matches=pd.read_csv('D:\python\data sets\world cup\WorldCupMatches.csv')
players=pd.read_csv('D:\python\data sets\world cup\WorldCupPlayers.csv')
wc=pd.read_csv('D:\python\data sets\world cup\WorldCups.csv')
'''explore matches dataset'''
print(matches.head())
print(matches.dtypes)
print(matches.columns)
print(matches.shape)

'''explore world cup dataset'''
print(wc.head())
print(wc.columns)
print(wc.dtypes)
print(wc.shape)

'''explore players dataset'''

print(players.head())
print(players.shape)
print(players.columns)
print(players.shape)

'''working with the world cup data'''
print(wc.isnull().sum())
print(wc.tail())
number_of_teams=wc.loc[:,['Year','QualifiedTeams']]
print(number_of_teams)
wc.rename(columns={"Runners-Up": "Second"},inplace=True)
print(wc.columns)

'''number of teams participating in world cup has been 32  since only year 1998'''

'''winners,runner ups and third place of each world cup'''
wc=wc.replace(to_replace='Germany FR',value='Germany')

'''to know first three places of every world cup'''
first_three=wc.loc[:,['Year','Winner','Second','Third']]
print(first_three)
'''number of winners of world cup, and ratio of winning'''
print(wc['Winner'].value_counts())
print(wc['Winner'].value_counts(normalize=True))
'''Brazil has won quarter of all played word cups,Only 8 different countries have won world cup'''
print(wc['Second'].value_counts())
'''Germany is the most team to be in second place with 4 times, followed by Netherlands and Germany each with 3 times'''

''' most teams in the first three places'''
best_three=pd.concat([wc.Winner,wc.Second,wc.Third])
print(best_three)
print(best_three.value_counts())
'''Germany is the most country to be in frist 3 places with 12 times out of 20 world cups'''

''' Graph showing winners of world cup'''
wc['Winner'].value_counts().plot(kind='bar')
plt.xlabel('Country')
plt.title('Countries won world cup')
plt.show()

print(wc.loc[:,['Year','MatchesPlayed','GoalsScored']])
'''2014 and 1998 have the most goals with 171 goals scored,while 1930 and 1934 have the least with 70'''
wc['average_goals']=wc['GoalsScored'].divide(wc['MatchesPlayed'])
print(wc['average_goals'])
print(wc.columns)

'''for average goals per match for each world cup'''
wc_avg=wc.loc[:,['Year','average_goals']]
wc_avg=wc_avg.sort_values(by=['average_goals'],ascending=False)
print(wc_avg)
'''1954 world cup has the highest average of scored goals per match with 5.3, while 2014 world cup has only 2.67 '''

plt.plot(wc['Year'],wc['average_goals'])
plt.xlim([1934,2014])
plt.xlabel('year')
plt.ylabel('average goals')
plt.title('average goals scored per world cup')
plt.show()

'''For attendance'''
print(wc['Attendance'])
plt.plot(wc['Year'],wc['Attendance'])
plt.xlabel('year')
plt.xlim([1934,2014])
plt.ylabel('Attendance')
plt.title('Attendance per world cup')
plt.show()
'''attendance shows an increasing trend, 2014 world cup witnessed the highest attendance'''



'''working with the Matches data'''
print(matches.columns)
print(matches.dtypes)
print(matches.shape)
print(matches.head())

''' cleaning and adjusting data'''
matches['Datetime']=pd.to_datetime(matches['Datetime'])
print(matches['Datetime'].dtype)
print(matches.dtypes)
print(matches.tail())
matches=matches.dropna(subset=['Year'])
print(matches.tail())
print(matches.shape)
matches[['Year','Home Team Goals','Away Team Goals','Half-time Home Goals','Half-time Away Goals']]=matches[['Year','Home Team Goals','Away Team Goals','Half-time Home Goals','Half-time Away Goals']].astype('int')
matches=matches.drop(['RoundID','MatchID','Assistant 1','Assistant 2'],axis='columns')
print(matches['Year'].dtype)
print(matches.head())
print(matches.loc[:,['Year','Home Team Name','Away Team Name','Win conditions']])
matches=matches.replace(to_replace='Germany FR',value='Germany')


print(matches.columns)


'''Creating a new column showing the winning team'''
def result(matches):
    if matches['Home Team Goals'] > matches['Away Team Goals']:
        return matches['Home Team Name']
    elif matches['Home Team Goals'] < matches['Away Team Goals']:
        return matches['Away Team Name']
    else:
        return 'tie'
matches['Winner']=matches.apply(result,axis=1)
print(matches.loc[:,['Year','Home Team Name','Away Team Name','Winner']])
print(matches['Winner'].value_counts())
'''Brazil has the highest number of winnings, followed by Germany with only 1 match difference'''

Brazil_matches= matches[matches['Home Team Name'].str.contains('Brazil') | matches['Away Team Name'].str.contains('Brazil')] 
print(Brazil_matches)
Germany_matches= matches[matches['Home Team Name'].str.contains('Germany') | matches['Away Team Name'].str.contains('Germany')] 
print(Germany_matches)
'''Brazil has played 108 matches in world cup,while Germany played 110'''

Germany_matches=Germany_matches.replace(to_replace='Germany FR',value='Germany')

def result(Brazil_matches):
    if (Brazil_matches['Home Team Goals'] > Brazil_matches['Away Team Goals'] ) and (Brazil_matches['Home Team Name'] == 'Brazil'):
        return 'Brazil wins'
    elif (Brazil_matches['Home Team Goals'] > Brazil_matches['Away Team Goals'] ) and (Brazil_matches['Away Team Name'] == 'Brazil'):
        return 'Brazil loses'
    elif (Brazil_matches['Home Team Goals'] < Brazil_matches['Away Team Goals'] ) and (Brazil_matches['Away Team Name'] == 'Brazil'):
        return 'Brazil wins'
    elif (Brazil_matches['Home Team Goals'] < Brazil_matches['Away Team Goals'] ) and (Brazil_matches['Home Team Name'] == 'Brazil'):
        return 'Brazil loses'
    else:
        return 'tie'
'''Brazil winning percentage of all matches'''
Brazil_matches['Result'] = Brazil_matches.apply(result, axis = 1)
print(Brazil_matches.loc[:,['Year','Home Team Name','Away Team Name','Result']])
print(Brazil_matches['Result'].value_counts())
print(Brazil_matches['Result'].value_counts(normalize=True))

def result(Germany_matches):
    if (Germany_matches['Home Team Goals'] > Germany_matches['Away Team Goals'] ) and (Germany_matches['Home Team Name'] == 'Germany'):
        return 'Germany wins'
    elif (Germany_matches['Home Team Goals'] > Germany_matches['Away Team Goals'] ) and (Germany_matches['Away Team Name'] == 'Germany'):
        return 'Germany loses'
    elif (Germany_matches['Home Team Goals'] < Germany_matches['Away Team Goals'] ) and (Germany_matches['Away Team Name'] == 'Germany'):
        return 'Germany wins'
    elif (Germany_matches['Home Team Goals'] < Germany_matches['Away Team Goals'] ) and (Germany_matches['Home Team Name'] == 'Germany'):
        return 'Germany loses'
    else:
        return 'tie'
'''Germany winning percentage of all matches'''
Germany_matches['Result']=Germany_matches.apply(result,axis=1)
print(Germany_matches.loc[:,['Year','Home Team Name','Away Team Name','Result']])
print(Germany_matches['Result'].value_counts())
print(Germany_matches['Result'].value_counts(normalize=True))
'''Brazil has highest number of wins, also Brazil has higher winning percentage than Germany'''

'''to see if the winner in first half wins the match'''
def results(matches):
    if (matches['Half-time Home Goals'] > matches['Half-time Away Goals']) and (matches['Home Team Goals'] > matches['Away Team Goals']):
        return 'winner at first half wins the match'
    elif (matches['Half-time Home Goals'] > matches['Half-time Away Goals']) and (matches['Home Team Goals'] < matches['Away Team Goals']):
         return 'winner at first half loses the match'
    elif (matches['Half-time Home Goals'] > matches['Half-time Away Goals']) and (matches['Home Team Goals'] == matches['Away Team Goals']):
        return 'winner at first half ties'
    elif (matches['Half-time Home Goals'] < matches['Half-time Away Goals']) and (matches['Home Team Goals'] < matches['Away Team Goals']):
        return 'winner at first half wins the match'
    elif (matches['Half-time Home Goals'] < matches['Half-time Away Goals']) and (matches['Home Team Goals'] > matches['Away Team Goals']):
        return 'winner at first half loses the match'
    elif (matches['Half-time Home Goals'] < matches['Half-time Away Goals']) and (matches['Home Team Goals'] == matches['Away Team Goals']):
        return 'winner at first half ties'
    elif (matches['Half-time Home Goals'] == matches['Half-time Away Goals']) and (matches['Home Team Goals'] == matches['Away Team Goals']):
        return 'the result was tie and remained tie'
    else:
        return 'first half is tie and the result changed after first half'
matches['difference between first and second half']=matches.apply(results,axis=1)
print(matches.loc[:,['Year','Home Team Name','Away Team Name','difference between first and second half']])

print(matches['difference between first and second half'].value_counts(normalize=True))
'''43.6% of winners at first half won the match, while only 4.5% of teams losing in the first half could perform a comeback and win'''

print(players.columns)
print(players.shape)
print(players.dtypes)
print(players.head())
players=players.drop(['RoundID','MatchID','Event'],axis='columns')
print(players.columns)
players=players.set_index('Player Name')
print(players.head())
print(players['Team Initials'].value_counts())

'''Brazil is the most country to be represented by different players with 2403 different players, followed by Italy'''
