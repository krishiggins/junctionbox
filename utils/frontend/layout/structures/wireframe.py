import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


class WireFrame():
    def __init__(self):
        self.header = dbc.Row(className="jumbotron",children=[dbc.Col(html.Div("Header Bar"), width=12)],style={'height':'1px'})

        #Placeholder for sidebar module
        self.sidebar = dbc.Col('Nav Bar', className='jumbotron')
        self.main_body = dbc.Col('Main Body', className="jumbotron")
        self.layout = html.Div(className="",
                        children=[
                            dbc.Container(className="",style={'height':'100vh'},
                               children=[self.header,
                                   dbc.Row([self.sidebar,
                                   self.main_body])
                                    ]),
                               ])

if __name__ == '__main__':
    import dash
    import themestore.themes as themes
    app = dash.Dash(external_stylesheets=[themes.BOOTSTRAP, themes.SOLAR])
    wire_frame = WireFrame()
    app.layout = html.Div(wire_frame.layout)
    app.run_server(debug=True)

