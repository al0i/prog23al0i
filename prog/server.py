# importar a biblioteca flask
from flask import Flask, jsonify
# biblioteca CORS
from flask_cors import CORS
# importar a classe Pessoa
from pessoa import *

# acesso ao flask via variável app
app = Flask(__name__)

# aplicando tratamento CORS ao flask
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)

# rota padrão
@app.route("/")
def ola():
    return "<b>Olá, gente!</b>"

# rota de listar pessoas
@app.route("/listar_pessoas")
def listar():
    # criar uma lista vazia para retorno das informações
    lista_retorno = []
    # criar uma lista de pessoas
    lista = [
        Pessoa(nome="João da Silva",
               nascimento="11/22/3333",
               email="josilva@gmail.com",
               telefone="47 99012 3232"),
        Pessoa(nome="Maria Oliveira",
               nascimento="11/22/3333",
               email="maliva@gmail.com",
               telefone="47 98823 4321"),
        Pessoa(nome="Teresa Soares",
               nascimento="11/22/3333",
               email="teso@gmail.com",
               telefone="47 98114 1423"),
    ]
    # percorrer a lista de pessoas
    for p in lista:
        # adicionar na lista de retorno a pessoa em formato json
        lista_retorno.append(p.json())

    # retornar a lista de pessoas json
    return jsonify(lista_retorno)

app.run(debug=True, host="0.0.0.0")

'''
resultado da invocação ao servidor:

curl localhost:5000/listar_pessoas
[
  {
    "email": "josilva@gmail.com",
    "nome": "Jo\u00e3o da Silva",
    "telefone": "47 99012 3232"
  },
  {
    "email": "maliva@gmail.com",
    "nome": "Maria Oliveira",
    "telefone": "47 98823 4321"
  },
  {
    "email": "teso@gmail.com",
    "nome": "Teresa Soares",
    "telefone": "47 98114 1423"
  }
]

'''