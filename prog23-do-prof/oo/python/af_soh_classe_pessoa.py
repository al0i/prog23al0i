# definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    # método que expressa o objeto em formato textual        
    def __str__(self): 
        # retorna uma string bonitinha :-)
        return self.nome + ", " + self.email + ", " + self.telefone