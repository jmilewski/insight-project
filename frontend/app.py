import os
import pathlib
import numpy as np
import datetime as dt
import time
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from scipy.stats import rayleigh
from db.api import get_wind_data


GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 5000)

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server

#app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}
app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

app.layout = html.Div(
    [
        # header
        html.Div(
            [
                html.Div(
                    [
                        html.H4("ETHER INTRINSIC VALUE TRACKING", className="app__header__title"),
                        html.P(
                            "Change in Price-Metcalfe Ratio to estimate current direction of intrinsic value.",
                            className="app__header__title--grey",
                        ),
                    ],
                    className="app__header__desc",
                ),

            ],
            className="app__header",
        ),
        html.Div(
            [
                # wind speed
                html.Div(
                    [
                        html.Div(
                            [html.H6("Price-Metcalfe Ratio (PMR)", className="graph__title")]
                        ),
                        dcc.Graph(
                            id="wind-speed",
                            figure=dict(
                                layout=dict(
                                    plot_bgcolor=app_color["graph_bg"],
                                    paper_bgcolor=app_color["graph_bg"],
                                )
                            ),
                        ),
                        dcc.Interval(
                            id="wind-speed-update",
                            interval=int(GRAPH_INTERVAL),
                            n_intervals=0,
                        ),
                    ],
                    className="column wind__speed__container",
                ),
            ],
            className="app__content",
        ),
    ],
    className="app__container",
)


def get_current_time():
    """ Helper function to get the current time in seconds. """

    #now = dt.datetime.now()
    #total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    #return total_time
    total_time = int(round(time.time()*1000))
    return total_time


@app.callback(
    Output("wind-speed", "figure"), [Input("wind-speed-update", "n_intervals")]
)
def gen_wind_speed(interval):
    """
    Generate the wind speed graph.

    :params interval: update the graph based on an interval
    """

    total_time = get_current_time()
    df = get_wind_data(total_time - 600000, total_time)

    trace = dict(
        type="scatter",
        y=df["pmr"],
        line={"color": "#42C4F7"},
        hoverinfo="skip",
        error_y={
            "type": "data",
            "array": [], #df["pmr"]
            "thickness": 1.5,
            "width": 2,
            "color": "#B4E8FC",
        },
        mode="lines",
    )

    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
        height=700,
        xaxis={
            "range": [0, 200],
            "showline": True,
            "zeroline": False,
            "fixedrange": True,
            "tickvals": [0, 50, 100, 150, 200],
            "ticktext": ["200", "150", "100", "50", "0"],
            "title": "Time Elapsed (sec)",
        },
        yaxis={
            "range": [
                min(-2, min(df["pmr"])),
                max(0, max(df["pmr"])) # + max(df["SpeedError"])),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
            "nticks": max(6, round(df["pmr"].iloc[-1] / 10)),
        },
    )

    return dict(data=[trace], layout=layout)


if __name__ == "__main__":
    app.run_server(debug=True)
