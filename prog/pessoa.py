class Pessoa:
    def __init__(self,nome,idade,email,telefone):
        self.nome = str(nome)
        self.idade = int(idade)
        self.email = str(email)
        self.telefone = str(telefone)

    def __str__(self):
        return (f"Nome: {self.nome} - Idade: {self.idade} - E-mail: {self.email} - Telefone: {self.telefone}.")
    
    def json(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "telefone": self.telefone
        }