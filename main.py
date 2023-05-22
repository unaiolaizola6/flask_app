from flask import Flask, render_template
import altair as alt
from vega_datasets import data

app = Flask(__name__)

@app.route('/')
def index():
    # Cargar los datos
    cars = data.cars()

    # Crear el gráfico con Altair
    chart = alt.Chart(cars).mark_circle().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin'
    ).interactive()

    # Guardar el gráfico en un archivo HTML temporal
    chart.save('chart.html')

    # Renderizar la plantilla HTML con el gráfico
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)




