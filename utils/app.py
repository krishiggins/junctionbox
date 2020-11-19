import dash_html_components as html
import dash_core_components as dcc

from utils.server import app
from utils.callbacks import callbacks, page_content
from utils.layout.structures.sidebar import Sidebar

app.layout = html.Div([Sidebar().layout_insitu])