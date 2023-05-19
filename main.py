from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run()
