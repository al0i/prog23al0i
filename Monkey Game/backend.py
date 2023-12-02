from config import *
from table.player import *

@app.route('/')
def index():
    return "Operant backend"

@app.route('/ranking')
def ranking():
    data = db.session.query(PlayerDB).order_by(desc(PlayerDB.score)).all()

    if data:
        jsonList = [i.json() for i in data]
        okJson = {"result":"ok"}
        okJson.update({"details":jsonList})
        return jsonify(okJson)
    else:
        return jsonify({"result":"error", "details":"bad gateway"})

@app.route('/save_image', methods=['POST'])
def save_image():
    try:
        fileVal = request.files['files']
        imgFile = os.path.join(path, 'img/')
        complete = os.path.join(imgFile, 'monkey.png')
        fileVal.save(complete)
        r = jsonify({'result':'ok', 'details':fileVal.filename})
        print(path, imgFile)
    except Exception as e:
        r = jsonify({'result':'error', 'details':str(e)})

    return r
    
db.create_all()
CORS(app)
app.run(debug=True)