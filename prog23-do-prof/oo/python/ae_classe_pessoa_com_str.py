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

# informar dados fictícios para teste
nome = "João da Silva"
email = "josilva@gmail.com"
telefone = "47 91234-5678"
# criar a pessoa
nova = Pessoa(nome, email, telefone)
# exibir os dados
print(nova)

'''
resultado da execução:

João da Silva, josilva@gmail.com, 47 91234-5678
'''