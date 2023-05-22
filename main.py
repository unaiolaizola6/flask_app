from flask import Flask, render_template, request
import altair as alt
import pandas as pd
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    #conn = mysql.connector.connect(host="dbnfg5oyozhtpn", user='umdcgwdtmlpas', password="L4_3b^3@1q[b", database="dbnfg5oyozhtpn") 
    #cursor = conn.cursor()
    #cursor.execute("select * from data")
    #datos = cursor.fetchall()
    alumno = request.form.get('alumno')
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [3, 5, 2, 4, 6]
    })

    
    chart = alt.Chart(data).mark_line().encode(
        x='x',
        y='y'
    ).to_json()

    return render_template('test.html', chart=chart, alumno=alumno)

if __name__ == '__main__':
    app.run()






