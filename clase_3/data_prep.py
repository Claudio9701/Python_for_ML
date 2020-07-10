# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:13:41 2020

@author: USUARIO
"""

#%%
import pandas as pd
df_validation = pd.read_csv("C:\\Users\\USUARIO\\Desktop\\AT\\API_football\\outputs\\df_for_model.csv")
#%%
df_validation.head(), df_validation.columns, df_validation.shape

#%%
#df_validation["winner"] = df_validation["winner"].astype(str).replace({"0":"local", "1":"empate", "2":"visita"})
df_group = df_validation[["league", "winner", "fixture_id"]].groupby(["league", "winner"], as_index = False).count()
df_group = df_group.rename(columns = {"fixture_id":"partidos"})
leagues = ["Bundesliga 1", "Bundesliga 2", "Championship", "Premier League",
           "Primeira Liga", "Primera Division", "Segunda Division", "Serie A", "Serie B"]
df_group = df_group.loc[df_group["league"].isin(leagues)]
#df_group.to_excel("C:\\Users\\USUARIO\\Desktop\\AT\\Clases_Python\\Python_for_ML\\clase_3\\inputs\\league_winner.xlsx", index = False)
df_group
#%%

df_primera_div = df_validation.loc[(df_validation["league"] == 'Primera Division')]
df_primera_div
#df_validation.league.unique()

#%%
df_validation["total_goals"] = df_validation["match_home_goals"] + df_validation["match_away_goals"]
df_goals = df_validation[["fixture_id", "date", "league", "home_team", "away_team", "total_goals", "winner"]]
df_goals = df_goals.sample(frac = 0.1)
df_goals.reset_index (drop = True, inplace = True)
df_goals.to_excel("C:\\Users\\USUARIO\\Desktop\\AT\\Clases_Python\\Python_for_ML\\clase_3\\inputs\\matches_goals_winner.xlsx", index = False)
#%%

