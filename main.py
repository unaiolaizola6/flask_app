from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)

@app.route('/')
def index():
    st.write("hola")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
