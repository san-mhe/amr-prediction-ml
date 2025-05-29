import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

bar_df = pd.read_csv("figures/shap_bar_data.csv")
beeswarm_df = pd.read_csv("figures/shap_beeswarm_data.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("AMR Resistance SHAP Dashboard"),
    dcc.Dropdown(
        id="plot-type",
        options=[
            {"label": "Mean |SHAP| Bar", "value": "bar"},
            {"label": "SHAP Beeswarm", "value": "beeswarm"},
        ],
        value="bar",
        clearable=False,
    ),
    dcc.Graph(id="shap-graph")
])

@app.callback(
    dash.dependencies.Output("shap-graph", "figure"),
    dash.dependencies.Input("plot-type", "value")
)

def update_figure(plot_type):
    if plot_type == "bar":
        fig = px.bar(
            bar_df,
            x="gene",
            y="mean_abs_shap",
            title="Mean |SHAP| by Gene",
            labels={"mean_abs_shap": "Mean |SHAP|", "gene": "Gene"}
        )
    else:
        melted = beeswarm_df.melt(var_name="gene", value_name="shap_value")
        fig = px.strip(
            melted,
            x="shap_value",
            y="gene",
            title="SHAP Beeswarm Plot (sample-level)",
            orientation="h",
        )
    fig.update_layout(yaxis={"categoryorder":"total descending"})
    return fig

import xgboost
import sklearn
import jupyterlab
import shap
import matplotlib

if __name__ == "__main__":
 # Dash v2+ uses app.run(), not run_server()
 app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)

