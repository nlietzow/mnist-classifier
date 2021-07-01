import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from lib.image_processing import image_processing
import numpy as np
import tensorflow as tf

import os

model = tf.keras.models.load_model(os.path.abspath("app/mnist_model"))
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Upload(
            id="upload-image",
            children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=False,
        ),
        html.Div(id="output-image"),
        html.Div(id="output-prediction"),
    ]
)


@app.callback(
    Output("output-prediction", "children"), Input("upload-image", "contents")
)
def prediction(content):
    if content is not None:
        final_img = image_processing(
            content=content,
            temp_path=os.path.abspath("app/temp/image.jpg"),
        )
        y = model.predict(final_img)
        return np.argmax(y)


@app.callback(Output("output-image", "children"), Input("upload-image", "contents"))
def update_output(image):
    if image is not None:
        child = html.Img(src=image)
        return child


if __name__ == "__main__":
    app.run_server(debug=True, port=8000, host="0.0.0.0")
