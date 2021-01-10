import dash_html_components as html
import dash_core_components as dcc

from frontend.server import app
from frontend.callbacks import callbacks, page_content
from frontend.layout.structures.sidebar import Sidebar

app.layout = html.Div([Sidebar().layout_insitu])