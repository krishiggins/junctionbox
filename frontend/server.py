# from flask import Flask
from dash import Dash
from frontend.themestore import themes, templates

# server = Flask('scoringportal')
app = Dash(external_stylesheets=[themes.BOOTSTRAP, themes.DEFAULT, themes.FONTAWESOME])
