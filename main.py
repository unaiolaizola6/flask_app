from flask import Flask, render_template, request
import streamlit as st

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    nombre = request.form.get('nombre')
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")
    return render_template('test.html')

if __name__ == '__main__':
    app.run()



