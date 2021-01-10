"""
This app aims to create a nested sidebar structure similar to VSCode layout.
V1 will be a sidebar only with 3 main page links with icons and a settings link at the bottom
V2 will aim to expand on this with a nested sidebar section for each icon"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from utils.server import app


class Sidebar():
    def __init__(self):
        global app
        self.url = dcc.Location(id="url")
        self.icons = ['fa fa-home fa-1x','fa fa-cog fa-1x','fa fa-tachometer-alt fa-1x','fa fa-file fa-1x',]
        self.icon_text = ['Home','Settings','Score','Info']
        self.formated_icons = self.format_icons()
        self.nav1 = dbc.ButtonGroup(self.formated_icons[:-1], vertical=True)
        self.nav2 = dbc.ButtonGroup(self.formated_icons[-1], vertical=True)
        self.layout = dbc.Nav(className="navbar bg-dark",
                            style={'width':'4rem', 'height':'98vh', 'padding':"0"}, vertical=True, pills=True,
                        children=[self.nav1, self.nav2]
                )


        self.layout_insitu = html.Div(className="", style={'height':'100vh'}, children=[
            self.url,dbc.Col([dbc.Row(dbc.Nav(className="navbar bg-dark",style={'width':'100%', 'height':'2vh'})),dbc.Row([self.layout, dbc.Col(id='page-content',style={'padding':'0'})])])
        ])

    def format_icons(self):
        formatted_icons =[]
        for i, icon in enumerate(self.icons):
            icon = html.I(className=icon, id=f"sidebar-button-{i}")
            icon_cell = dbc.Row(dbc.Col(icon))
            text_cell = dbc.Row([dbc.Col(html.P(self.icon_text[i], className='small'),style={'padding':'0'})])

            button_contents = [icon_cell, text_cell]
            container = dbc.Button(className="btn btn-dark text-muted btn-ghost-secondary", id=f"page-{i}-link", style={'width':'3.5rem','height':'3.5rem','justify-content':'center'},
                                      children=button_contents)
            linked_container = dbc.NavLink(className='nav-item',href=f"/page-{i}", children=container, style={'padding':'0.1rem','margin':'0'})
            formatted_icons.append(linked_container)
        return formatted_icons


if __name__ == "__main__":
    import dash
    sidebar = Sidebar()
    app.layout = sidebar.layout_insitu
    app.run_server(port=8888, debug=True)

