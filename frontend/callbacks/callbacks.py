from frontend.server import app
from dash.dependencies import Input, Output, State

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(4)] +
    [Output(f"page-{i}-link", "disabled") for i in range(4)] +
    [Output(f"sidebar-button-{i}", "style") for i in range(4)]

    , [Input("url", "pathname")]
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        response = [True, False, False, False]
        print(response + [not (i) for i in response] + [{'color': 'red'} if i == True else {} for i in response])
        return response + [not (i) for i in response] + [{'color': 'red'} if i == True else {} for i in response]
    response = [pathname == f"/page-{i}" for i in range(4)]
    print(response + [not (i) for i in response] + [{'color': 'red'} if i == True else {} for i in response])
    return response + [not (i) for i in response] + [{'color': 'red'} if i == True else {} for i in response]

