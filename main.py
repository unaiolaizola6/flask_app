from flask import Flask, render_template, request
import streamlit as st

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    nombre = request.form.get('nombre')
    st.write(nombre)
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
