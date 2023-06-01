from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'animais.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    raca = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    genero = db.Column(db.String(30))

    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity':'animal', 
        'polymorphic_on':type
        }
    
    def __str__(self):
        return f'{self.nome} - {self.raca} - {self.cor} - {self.genero}'
    
class Gato(Animal):
    id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key=True)
    fugas = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity':'gato'
    }

    def __str__(self):
        return super().__str__() + f' - {self.fugas}'

class Cachorro(Animal):
    id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity':'cachorro'
    }
    
    def __str__(self):
        return super().__str__()

with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all()

    cachorro = Cachorro(nome="Jack", raca="Yorkshire", cor="Preto e marrom", genero="M")            

    db.session.add(cachorro)
    db.session.commit()

    gato = Gato(nome="Vanda", raca="Vira-lata", cor="Mista", genero="F", fugas=50)

    db.session.add(gato)
    db.session.commit()

    for p in db.session.query(Animal).all():
        print(p)

'''
    maria = Motorista(nome="Maria Oliveira", email="mari@gmail.com", 
                telefone="98813-1415", cnh="123-4")
    print(f'Motorista: {maria}')
    # Motorista: Maria Oliveira, 98813-1415, mari@gmail.com, CNH: 123-4
    db.session.add(maria)
    db.session.commit()

    # listando as pessoas :-)
    print("Listando pessoas:")
    for p in db.session.query(Pessoa).all():
        print(p)

    #Listando pessoas:
    #João da Silva, None, josilva@gmail.com
    #Maria Oliveira, 98813-1415, mari@gmail.com

    # Maria começou a vender também - lascou
    maria_vend = Vendedor(nome="Maria Oliveira", email="mari@gmail.com", 
                telefone="98813-1415", comissao = 15)
    print(f'Agora é vendedora :-/: {maria_vend}')
    db.session.add(maria_vend)
    db.session.commit()

    # zoeira no bd: Maria foi cadastrada 2 vezes na tabela pessoa'''