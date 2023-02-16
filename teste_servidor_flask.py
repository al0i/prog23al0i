from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def padrao():
    return '''Exemplo de servidor que retorna lista.<br>
    Ações: <a href="/lista_texto">TEXTO</a> | 
    <a href="/lista_json">JSON</a>'''

@app.route("/lista_texto")
def lista_texto():
    lista = ['Sapo', 'Mamaco', 'Peixe-boi']

    return lista

@app.route("/lista_json")
def lista_json():
    lista = ['Essa', 'é', 'a lista', 'em JASON MYERS!']
    return jsonify(lista)

app.run(debug=True, host='0.0.0.0', port=5000)