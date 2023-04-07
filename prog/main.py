from flask import Flask, jsonify, request
from flask_cors import CORS
from pessoa import Pessoa

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return open('./index.html', 'r')

@app.route('/incluir', methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        nova = Pessoa(**dados)
        return jsonify({"resultado":"ok"})
    except Exception as e:
        return jsonify({"resultado":"erro","detalhes":str(e)})

@app.route('/listar')
def listar():
    lista_retorno = []
    lista = [
        Pessoa(nome="João",
               idade=16,
                email="joao@email.com",
                telefone="(47) 99191-9191"
               ),
        Pessoa(nome="Maíra",
               idade=17,
                email="maira@email.com",
                telefone="(47) 91212-1212"
               ),
        Pessoa(nome="Edilene",
               idade=45,
               email="edilene@email.com",
               telefone="(47) 9 1234-5678"
               )
    ]
    for p in lista:
        lista_retorno.append(p.json())

    return jsonify(lista_retorno)

app.run(debug=True)#, host='0.0.0.0')