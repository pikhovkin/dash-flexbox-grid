import dash_flexbox_grid as dfx
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = dfx.Grid(fluid=True, children=[
    dfx.Row(children=[
        dfx.Col(xs=12, children=[html.Div('Hello,'), html.Div('World!')])
    ]),
    dfx.Row(children=[
        dfx.Col(xs=6, children=html.Div('Hello, World!')),
        dfx.Col(xs=6, children=html.Div('Hello, World!'))
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
