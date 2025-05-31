import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import base64
from io import BytesIO
from PIL import Image  # ✅ This one
import matplotlib.image as mpimg



bar_df = pd.read_csv("figures/shap_bar_data.csv")
beeswarm_df = pd.read_csv("figures/shap_beeswarm_data.csv")

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("AMR Resistance SHAP Dashboard"),

    html.Label("Select Visualization:"),
    dcc.Dropdown(
        id="plot-type",
        options=[
            {"label": "Mean |SHAP| Bar", "value": "bar"},
            {"label": "SHAP Beeswarm", "value": "beeswarm"},
            {"label": "Confusion Matrix", "value": "confusion"},
        ],
        value="bar",
        clearable=False,
    ),

    html.Br(),
    dcc.Graph(id="shap-graph")
])



@app.callback(
    Output("shap-graph", "figure"),
    Input("plot-type", "value")
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
        fig.update_layout(yaxis={"categoryorder": "total descending"})

    elif plot_type == "beeswarm":
        melted = beeswarm_df.melt(var_name="gene", value_name="shap_value")
        fig = px.strip(
            melted,
            x="shap_value",
            y="gene",
            title="SHAP Beeswarm Plot (sample-level)",
            orientation="h"
        )
        fig.update_layout(yaxis={"categoryorder": "total descending"})



    elif plot_type == "confusion":

        # Load and encode image

        img_array = mpimg.imread("figures/confusion_matrix.png")

        img_pil = Image.fromarray((img_array * 255).astype("uint8")) if img_array.dtype != "uint8" else Image.fromarray(
            img_array)

        buffered = BytesIO()

        img_pil.save(buffered, format="PNG")

        encoded_image = base64.b64encode(buffered.getvalue()).decode()

        # Create figure with expanded axis range

        fig = go.Figure()

        fig.add_layout_image(

            dict(

                source="data:image/png;base64," + encoded_image,

                xref="x",

                yref="y",

                x=0,

                y=10,  # Larger y-range

                sizex=10,

                sizey=10,

                sizing="contain",

                opacity=1,

                layer="below"

            )

        )

        fig.update_xaxes(visible=False, range=[0, 10])  # Adjust x range

        fig.update_yaxes(visible=False, range=[0, 10])  # Adjust y range

        fig.update_layout(title="Model Confusion Matrix", height=600)

    else:
        fig = go.Figure()

    return fig

import xgboost
import sklearn
import jupyterlab
import shap
import matplotlib


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)



