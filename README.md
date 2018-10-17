# dash-flexbox-grid

Wrapper around [react-flexbox-grid][] for Plotly [Dash][]

## Usage

```python

    import dash
    import dash_flexbox_grid as dfx
    import dash_html_components as html
    
    
    app = dash.Dash('')
    app.scripts.config.serve_locally = True
    
    app.layout = dfx.Grid(id='grid', fluid=True, children=[
        dfx.Row(children=[
            dfx.Col(xs=12, lg=3, children=[
                html.Div('Hello,'), html.Div('World!')
            ])
        ]),
        dfx.Row(id='row', children=[
            dfx.Col(id='col', xs=6, lg=2, children=html.Div('Hello, World!')),
            dfx.Col(xs=6, lg=2, children=html.Div('Hello, World!'))
        ])
    ])
    
    
    if __name__ == '__main__':
        app.run_server(debug=True)

```

## Dash

Go to this link to learn about [Dash][].

See the [dash-component-boilerplate][] repo for more information.

[react-flexbox-grid]: https://github.com/roylee0704/react-flexbox-grid
[Dash]: https://github.com/plotly/dash
[dash-component-boilerplate]: https://github.com/plotly/dash-component-boilerplate
