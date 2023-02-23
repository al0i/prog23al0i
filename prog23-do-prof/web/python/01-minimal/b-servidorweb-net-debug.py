from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola():
    return "Servidor de Hylson disponível na rede"

app.run(debug=True, host="0.0.0.0", port=4999)

# debug: alterações no código reiniciam o servidor web
# host: o servidor está disponível para acesso na rede
# port: o servidor fica disponível em porta diferente da padrão

# teste com curl: 191.52.7.10:4999
