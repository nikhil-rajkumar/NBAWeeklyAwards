import pandas as pd
import numpy as np
import operator
#import matplotlib.pyplot as plt
#import seaborn as sns


stats_df = pd.read_csv('Ball - Jan 3-9.csv')
dic = {}
#print(type(stats_df))
#print(stats_df)

#Converting column of names to list
lst = stats_df['PLAYER'].astype(str).values.tolist()
#print(lst)

#Converting names to dictionary for getting count
for person in lst:
    if person not in dic:
        dic[person]=0
    dic[person] += 1
#print(dic)

#Sorting dictionary into descending order to get top recurring players
sorted_dic = dict(sorted(dic.items(), key=operator.itemgetter(1),reverse=True))
#print(sorted_dic)

#Filtering out top players into list
top = sorted_dic.values()
top = max(top)
#print(top)

#Get all players with max recurrence into a list 
top_players = []
for play in sorted_dic:
    if sorted_dic[play] == top:
        top_players.append(play)
#print(top_players)

#Create an avg of ESPN, DScore, and OScore of each player and store in a dictionary with key:value, key -> name and value-> array of each avg score
new_df = stats_df[stats_df['PLAYER'].isin(top_players)]
#print(type(new_df))
new_df = new_df.loc[:, ["PLAYER", "ESPN", "DScore", "OScore", "PTS", "REB", "AST", "BLK", "STL", "TO"]]
new_df = new_df.groupby("PLAYER").mean()
print(new_df)

#Printing out the final award winners
print()
print("ESPN Weekly MVP: ", new_df['ESPN'].max())
print("Defensive Player of the Week", new_df['DScore'].max())
print("Offensive Player of the Week", new_df['OScore'].max())