from pessoa import *

# teste da classe
p1 = Pessoa(nome = "João da Silva", 
            nascimento="11/22/3333",
            email = "josilva@gmail.com",  
            telefone = "47 99012 3232")
            
# exibir em formato textual
print(p1)

# exibir em format json
print(p1.json())

'''
resultado da execução:

João da Silva, josilva@gmail.com, 47 99012 3232
{'nome': 'João da Silva', 'email': 'josilva@gmail.com', 'telefone': '47 99012 3232'}

'''