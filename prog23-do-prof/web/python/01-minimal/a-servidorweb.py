from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola():
    return "<b>Olá, gente!</b>"

app.run()

# referência: https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application    
# acesso: curl localhost:5000, ou no navegador web: localhost:5000
