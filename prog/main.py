from flask import Flask, jsonify, request
from flask_cors import CORS
from pessoa import Pessoa

app = Flask(__name__)
CORS(app)
listaPessoas = []

@app.route('/')
def index():
    return open('index.html', 'r')

@app.route('/incluir', methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        nova = Pessoa(**dados)
        listaPessoas.append(nova)
        return jsonify({"resultado":"ok"})
    except Exception as e:
        return jsonify({"resultado":"erro","detalhes":str(e)})

@app.route('/listar')
def listar():
    lista_retorno = []
    for p in listaPessoas:
        lista_retorno.append(p.json())
    
    return jsonify(lista_retorno)

app.run(debug=True)#, host='0.0.0.0')