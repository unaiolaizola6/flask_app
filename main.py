from flask import Flask, render_template, request
import streamlit as st

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    nombre = request.form.get('nombre')
    return nombre

@app.route('/')
def streamlit():
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")

if __name__ == '__main__':
    app.run()
