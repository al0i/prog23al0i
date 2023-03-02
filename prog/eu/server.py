from flask import Flask, jsonify
from classePessoa import Pessoa
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def ola():
    return "<h1>Olá mundo!</h1>"

@app.route("/listar")
def listar():
    lista = [
        Pessoa("Matheus Joenck", "matheusjoenck@email.com"),
        Pessoa("Bárbara Müller", "barbara@email.com")
    ]

    listaRetorno = []
    for p in lista:
        listaRetorno.append(p.json())
    
    return jsonify(listaRetorno)

app.run(debug=True)