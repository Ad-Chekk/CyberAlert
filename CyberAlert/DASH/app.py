from dash import html, dcc
from dash.dependencies import Input, Output
from DASH.pages.page2 import create_page_2
from DASH.pages.page3 import create_page_3
from DASH.pages.page4 import create_page_4
import dash
import dash_bootstrap_components as dbc

from DASH.navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to home page!')


def create_page_home():
    layout = html.Div([
        nav,
        header,
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


server = app.server
app.config.suppress_callback_exceptions = True


app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return create_page_2()
    if pathname == '/page-3':
        return create_page_3(app)
    if pathname == '/page-4':
        return create_page_4(app)
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=True, port=8060  )

  