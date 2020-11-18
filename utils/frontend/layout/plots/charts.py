import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px

import themestore.themes as themes
import utils.frontend.themes.templates

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

app = dash.Dash(external_stylesheets=[themes.BOOTSTRAP, themes.DEFAULT, themes.FONTAWESOME])


class Charts():
    def __init__(self):
        global app
        self.time_series_df = pd.DataFrame()
        self.time_series_df['date'] = [(datetime.datetime.now()+relativedelta(months=i)).date() for i in range(7)]*3
        self.time_series_df['color'] =  ['violet' for i in range(7)]+['teal' for i in range(7)]+['red' for i in range(7)]
        self.time_series_df['type'] = ['bar' for i in range(14)] + ['line' for i in range(7)]
        self.time_series_df['counts'] = [73, -63, -12, 76, 77, 70, 17]+[-30, 80, 20, 60, 38, -76, 22]+[-45, -70, 2, -79, 71, 64, -50]
        self.barchart = px.bar(self.time_series_df[self.time_series_df['type']=='bar'], x='date', y='counts', color='color', barmode='group')
        self.barchart.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")

        self.graph = dcc.Graph(figure=self.barchart)
        self.layout = html.Div(self.graph)


if __name__ == "__main__":
    import dash
    charts = Charts()
    app.layout = charts.layout
    app.run_server(port=8888, debug=True)

