from flask import Flask, render_template, request
import altair as alt
import pandas as pd
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    conn = mysql.connector.connect(host="c47244.sgvps.net", user='umdcgwdtmlpas', password="L4_3b^3@1q[b", database="dbnfg5oyozhtpn") 
    cursor = conn.cursor()
    cursor.execute("select * from sentiments")
    datos = cursor.fetchall()
    alumno = request.form.get('alumno')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [3, 5, 2, 4, 6]
    })

    
    chart = alt.Chart(data).mark_line().encode(
        x='x',
        y='y'
    ).to_json()

    return render_template('test.html', chart=chart, alumno=alumno, nombre=nombre, apellido=apellido, datos=datos)

if __name__ == '__main__':
    app.run()






