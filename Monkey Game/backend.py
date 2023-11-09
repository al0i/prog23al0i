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
    
@app.route('/save_image', methods=['POST'])
def salvar_imagem():
    try:
        file_val = request.files['foto']
        arquivoimg = os.path.join(fileDB, 'img/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes":file_val.filename})
    except Exception as e:
        r = jsonify({"resoltado":'erro', 'detalhes':str(e)})
    
    return r

@app.route('/get_image/<int:id_player>')
def get_image(id_player):
    p = db.session.get(PlayerDB, id_player)
    completo = os.path.join('img/'+p.image)
    return send_file(completo, mimetype='image/gif')

@app.route("/incluir_player", methods=['post'])
def incluir_player():
    dados = request.get_json(force=True)
    try:
        nova = PlayerDB(**dados)
        db.session.add(nova)
        db.session.commit()
        return jsonify({'resultado':'ok', 'detalhes':'oi'})
    except Exception as e:
        return jsonify({'resultado':'erro', 'detalhes':str(e)})
    
@app.route('/retornar_players')
def retornar_players():
    try:
        players = db.session.query(PlayerDB).all()
        players_json = [x.json() for x in players ]
        retorno = {'resultado':'ok'}
        retorno.update({'detalhes':players_json})
        return jsonify(retorno)
    except Exception as e:
        return jsonify({'resultado':'erro', 'detalhes':str(e)})

db.create_all()
CORS(app)
app.run(debug=True)