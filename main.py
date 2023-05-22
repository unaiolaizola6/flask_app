from flask import Flask, render_template
import streamlit as st
from streamlit.server.server import Server

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/streamlit')
def streamlit():
   st.set_page_config(page_title="My Streamlit App")
   st.write("Hello, world!")

if __name__ == '__main__':
   server = Server(app)
   server.start()
   server.io_loop.start()
