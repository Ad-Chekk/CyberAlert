from DASH.navbar import create_navbar
from dash import html, dcc

nav = create_navbar()
header = html.H3('Welcome to page 4!')
def create_page_4(app):
    
    
    styles = {
    'gradient-background': {
        'background': 'linear-gradient(to right, #000000, #00000f, #00005f)',
        'min-height': '100vh',
        'padding': '20px',
        'display': 'flex',  # Changed to flex for sidebar layout
    },
    }
    layout= html.Div(
        style=styles['gradient-background'],
        
        children=
        [
        nav,
    ])
    return layout