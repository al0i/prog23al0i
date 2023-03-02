class Pessoa:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f'{self.nome}, {self.email}'
    
    def json(self):
        return{
            "nome" : self.nome,
            "email" : self.email
        }