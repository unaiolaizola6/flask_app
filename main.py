from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)
@app.route('/', methods=['POST'])
def index():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
