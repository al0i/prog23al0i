import pygame, os, random, time
from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import desc

app = Flask(__name__)
CORS(app)
path = os.path.dirname(os.path.abspath(__file__))
fileDB = os.path.join(path, 'table/players.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+fileDB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()