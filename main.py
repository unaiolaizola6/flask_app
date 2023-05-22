from flask import Flask, render_template, request
import streamlit as st

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recibir_datos():
    nombre = request.form.get('nombre')
    # Procesar el valor recibido y mostrarlo en Streamlit
    st.write(f"El nombre recibido es: {nombre}")

if __name__ == '__main__':
    app.run()



