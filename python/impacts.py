#!/usr/bin/env python3
#####################################
#    LAST UPDATED     09 MAR 2021   #
#####################################
"""
Use Plotly for aircraft data analysis. Data from
https://catalog.data.gov/dataset/p-3-meteorological-and-navigation-data-impacts-v1
https://catalog.data.gov/dataset/er-2-navigation-data-impacts-v1

"""
import plotly.graph_objects as go
import pandas as pd

list_of_files = [
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200115_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200118_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200125_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200201_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200205_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200207_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200223_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200225_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200227_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200302_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200112_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200118_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200125_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200201_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200205_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200207_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200213_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200218_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200220_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200224_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200225_R0.csv']

for i in range(len(list_of_files)):
    df = pd.read_csv(list_of_files[i])
    df['Longitude'] = df['Longitude'].replace(-9999.0, None)
    df['Latitude'] = df['Latitude'].replace(-9999.0, None)
    fig = go.Figure()
    counter = 30
    fig.add_trace(go.Scattermapbox(mode="lines", lat=df['Latitude'].dropna(),
                                   lon=df['Longitude'].dropna(), showlegend=False,
                                   line={'color': 'gray'},
                                   name=""))
    fig.add_trace(go.Scattermapbox(mode="markers+lines", lon=df['Longitude'].head(counter).dropna(),
                                   lat=df['Latitude'].head(counter).dropna(),
                                   showlegend=True,
                                   marker={'size': 6, 'color': 'blue'},
                                   name="Start"))
    fig.add_trace(go.Scattermapbox(mode="markers+lines", lon=df['Longitude'].tail(counter).dropna(),
                                   lat=df['Latitude'].tail(counter).dropna(),
                                   showlegend=True,
                                   marker={'size': 6, 'color': 'red'},
                                   name="End"))
    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={'center': {'lon': -100, 'lat': 40},
                'style': "carto-positron",
                'zoom': 3},
        geo_scope="usa")
    fig.show()
