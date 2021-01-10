from frontend.server import app
from frontend.layout.plots.charts import Charts

from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-0"]:
        return html.H1("Portal", className="blockquote text-center")
    elif pathname == "/page-1":
        return [html.H1("Placeholder for a cool mixboard-style-thing", className="blockquote text-center"), \
               html.Div(className ="form-group has-success",children=[
                   html.Label("Valid input", className="form-control-label", htmlFor="inputValid"),
                   dbc.Input(placeholder="A model option", className="form-control is-valid", style={'width':'20rem'}),\
                    html.Div("Success! You've done it",className="valid-feedback")
                        ])]

    elif pathname == "/page-2":
        return html.H1(className="blockquote text-center", children=["All the metrics",Charts().layout])
    elif pathname == "/page-3":
        return [html.P("Some links to pages", className="blockquote text-center"),html.H1(html.A("Hompage", href='https://google.com'), className="blockquote text-center")]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )