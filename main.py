from flask import Flask, render_template
import altair as alt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Crear los datos
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [3, 5, 2, 4, 6]
    })

    # Crear el gráfico de líneas
    chart = alt.Chart(data).mark_line().encode(
        x='x',
        y='y'
    ).to_json()

    return render_template('index.html', chart=chart)

if __name__ == '__main__':
    app.run()






