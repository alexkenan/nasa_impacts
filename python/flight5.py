import plotly.graph_objects as go
import pandas as pd

list_of_files = [
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_ER2_20200205_R0.csv',
    'https://raw.githubusercontent.com/alexkenan/nasa_impacts/main/datasets/IMPACTS_MetNav_P3B_20200205_R0.csv']

fig = go.Figure()
counter = 1

df = pd.read_csv(list_of_files[0])
fig.add_trace(go.Scattermapbox(mode="lines", lon=df['Longitude'], lat=df['Latitude'], showlegend=True,
                               line={'color': 'orange'},
                               name="ER-2"))
fig.add_trace(go.Scattermapbox(mode="markers", lon=df['Longitude'].head(counter),
                               lat=df['Latitude'].head(counter),
                               showlegend=False,
                               marker={'size': 10, 'color': 'darkgreen'},
                               name=""))

df = pd.read_csv(list_of_files[1])
fig.add_trace(go.Scattermapbox(mode="lines", lon=df['Longitude'], lat=df['Latitude'], showlegend=True,
                               line={'color': 'blue'},
                               name="P-3B"))
fig.add_trace(go.Scattermapbox(mode="markers", lon=df['Longitude'].head(counter),
                               lat=df['Latitude'].head(counter),
                               showlegend=False,
                               marker={'size': 10, 'color': 'darkgreen'},
                               name=""))

fig.update_layout(
    margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
    mapbox={'center': {'lon': -100, 'lat': 40},
            'style': "carto-positron",
            'zoom': 4},
    geo_scope="usa")
fig.show()
