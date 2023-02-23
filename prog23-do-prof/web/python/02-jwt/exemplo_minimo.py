from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# acesso ao flask
app = Flask(__name__)

# configuração da senha secreta da apicação
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
# acesso à biblioteca jwt
jwt = JWTManager(app)

# rota para autenticação
@app.route("/login", methods=["POST"])
def login():
    # receber os parâmetros
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # validação estática de login e senha
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    # criar a json web token (JWT)
    # essa JWT armazena o nome do usuário
    # sob ao nome "identity"
    access_token = create_access_token(identity=username)

    # retornar a token
    return jsonify(access_token=access_token)

# rota protegida, JWT é requerida
@app.route("/protected", methods=["GET"])
@jwt_required() # anotação que define rota protegida
def protected():
    # obtém a identidade de quem está logado
    # se não está logado, a requisição é negada
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

app.run()

'''

$ curl localhost:5000/protected
{"msg":"Missing Authorization Header"}

$ curl -X POST localhost:5000/login -d '{"username":"test","password":"test"}' -H 'Content-Type: application/json'
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODMxMzcyNiwianRpIjoiYTU1ZWUxZWItNWE0Yy00ODEyLThmZGUtMjY0YmY1M2MzNGRiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE2NTgzMTM3MjYsImV4cCI6MTY1ODMxNDYyNn0.kG2au9uMC9vn0iSSp4eHCCdCbXFaHeIlpDvhO_8zOxE"}

$ curl localhost:5000/protected -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODMxMzcyNiwianRpIjoiYTU1ZWUxZWItNWE0Yy00ODEyLThmZGUtMjY0YmY1M2MzNGRiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE2NTgzMTM3MjYsImV4cCI6MTY1ODMxNDYyNn0.kG2au9uMC9vn0iSSp4eHCCdCbXFaHeIlpDvhO_8zOxE'
{"logged_in_as":"test"}

'''    