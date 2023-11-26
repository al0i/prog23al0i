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
    
###############################
@app.route('/save_image', methods=['POST'])
def salvar_imagem():
    try:
        file_val = request.files['files']
        arquivoimg = os.path.join(path, 'img/')
        completo = os.path.join(arquivoimg, 'monkey.png')
        file_val.save(completo)
        r = jsonify({'resultado':'ok', 'detalhes':file_val.filename})
        print(path, arquivoimg)
    except Exception as e:
        r = jsonify({'resultado':'erro', 'detalhes':str(e)})

    return r
    
db.create_all()
CORS(app)
app.run(debug=True)