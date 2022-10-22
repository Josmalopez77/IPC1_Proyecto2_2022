from flask import Flask
from flask_cors import CORS
from flask.globals import request
from Album_DAO import Album_DAO
from flask import jsonify
import json

cl = Album_DAO()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {"msg" : "This api works!"}

@app.route('/album', methods=['POST'])
def book2():
    response={}
    id=request.json['id']
    name=request.json['name']
    created_at=request.json['created_at']
    if(cl.Crear(id, name, created_at)):
        response={
            "Message": "Albúm creado"
        }
        return response
    else:
        response={
            "Message": "Error"
        },500
        return response
    
@app.route('/album', methods=['GET'])
def person3():
    resp = cl.Mostrar_Album()
    response={}
    if(resp!=False):
        return jsonify(resp)
    else:
        response={
            "Message": "Error"
        },500
        return response
    
if __name__ == '__main__':
    app.run(threaded=True ,port=5000, debug=True)
    
