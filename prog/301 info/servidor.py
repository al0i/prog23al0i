from flask import Flask, jsonify
from flask_cors import CORS
from pessoa import Pessoa

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return open('./index.html', 'r')

@app.route("/barbara")
def barbara():
    lista_retorno = []
    lista = [
        Pessoa("Matheus","matheus@email.com"),
        Pessoa("Bárbara", "barbara@email.com"),
        Pessoa("Anderson", "anderson.coordenador@email.com")
    ]
    for p in lista:
        lista_retorno.append(p.json())

    return jsonify(lista_retorno)

app.run()