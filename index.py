from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recibir_datos():
    nombre = request.form.get('nombre')
    print(nombre)

if __name__ == '__main__':
    app.run()
