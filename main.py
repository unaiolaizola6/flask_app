from flask import Flask, render_template, request
import altair as alt
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recibir_datos():
    nombre = request.form.get('nombre')
    # Procesar el valor recibido y mostrarlo en Streamlit
    x = np.arange(100)
    source = pd.DataFrame({
      'x': x,
      'f(x)': np.sin(x / 5)
    })

    alt.Chart(source).mark_line().encode(
        x='x',
        y='f(x)'
    )

if __name__ == '__main__':
    app.run()



