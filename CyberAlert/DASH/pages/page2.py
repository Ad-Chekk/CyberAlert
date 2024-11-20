from dash import html, dcc
import plotly.graph_objects as go
from DASH.navbar import create_navbar
import json
import requests
import numpy as np

# Create the navigation bar
nav = create_navbar()

# Header for the page
header = html.H3('Welcome to page 2!')

def create_3d_globe_with_borders():
    # Load GeoJSON data for country borders
    url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
    geojson_data = requests.get(url).json()

    # Create the 3D globe
    fig = go.Figure()

    # Add surface for the globe
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    fig.add_trace(go.Surface(
        x=x, y=y, z=z,
        colorscale="Blues",
        showscale=False,
        opacity=0.7
    ))

    # Add country borders
    for feature in geojson_data["features"]:
        coordinates = feature["geometry"]["coordinates"]
        if feature["geometry"]["type"] == "Polygon":
            for polygon in coordinates:
                add_country_border(fig, polygon)
        elif feature["geometry"]["type"] == "MultiPolygon":
            for multipolygon in coordinates:
                for polygon in multipolygon:
                    add_country_border(fig, polygon)

    # Set layout for 3D visualization
    fig.update_layout(
        title="3D Globe with Country Borders",
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode="data",
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        margin=dict(l=0, r=0, t=40, b=0),
        height=700,
        width=700
    )

    return fig


def add_country_border(fig, polygon):
    # Convert longitude and latitude to 3D coordinates
    lon, lat = zip(*polygon)
    x = 10 * np.cos(np.radians(lat)) * np.cos(np.radians(lon))
    y = 10 * np.cos(np.radians(lat)) * np.sin(np.radians(lon))
    z = 10 * np.sin(np.radians(lat))

    # Add line trace for the border
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="lines",
        line=dict(color="black", width=1),
        name="Country Borders",
        showlegend=False
    ))


def create_page_2():
    layout = html.Div(
        style={
            'backgroundColor': 'black',  # Set the background color to black
            'height': '100vh',           # Full height of the viewport
            'color': 'white',             # Set text color to white for visibility
            'display': 'flex',
            'flexDirection': 'column',
            #'alignItems': 'center',
            #'justifyContent': 'center'
        },
        children=
        [
        nav,
        header,
        dcc.Graph(
            id='globe',
            figure=create_3d_globe_with_borders(),
             style={'backgroundColor': 'black'},
            
        )
    ])
    return layout
