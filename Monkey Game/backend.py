from config import *
from player import *

@app.route('/')
def index():
    return "Operant backend"

@app.route('/ranking')
def listar():
    data = db.session.query(PlayerDB).all()
    if data:
        jsonList = [i.json() for i in data]
        okJson = {"result":"ok"}
        okJson.update({"details":jsonList})
        return jsonify(okJson)
    else:
        return jsonify({"result":"error", "details":"bad gateway"})
    
db.create_all()
CORS(app)
app.run(debug=True)