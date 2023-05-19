from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    nombre = request.form.get('nombre')
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
