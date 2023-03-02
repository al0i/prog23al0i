class Pessoa:
    # construtor com valor padrão nos parâmetros
    def __init__(self, nome="", email="", telefone="", nascimento=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nascimento = nascimento

    # expressar a classe em formato texto
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.nascimento}, {self.email}, {self.telefone}'

    # expressar a classe em formato json
    def json(self):
        return {
            "nome" : self.nome,
            "nascimento" : self.nascimento,
            "email" : self.email,
            "telefone" : self.telefone 
        }