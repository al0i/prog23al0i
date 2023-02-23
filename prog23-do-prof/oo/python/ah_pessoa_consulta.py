# definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, email, telefone, tps, dt_nasc):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.tipo_sanguineo = tps
        self.data_nascimento= dt_nasc
    # no método a seguir, vamos usar uma formação de string
    # com o 'f', que permite usar variáveis dentro da string,
    # e com os triplos apóstrofos, que permite posicionar livremente
    # os conteúdos onde eles devem aparecer
    def __str__(self): 
        return f'''
        Nome: {self.nome}, 
        Email: {self.email}, 
        Telefone: {self.telefone}
        Tipo sanguíneo: {self.tipo_sanguineo}, 
        Nascido(a) em: {self.data_nascimento}'''

# informar dados fictícios para teste
nome = "João da Silva"
email = "josilva@gmail.com"
telefone = "47 91234-5678"
tipo_sang = "O+"
nasc = "28/10/1988"
# criar a pessoa
nova = Pessoa(nome, email, telefone, tipo_sang, nasc)
# exibir os dados
print("*** Teste da classe Pessoa:\n", nova)

class Consulta:
    def __init__(self, data, hora, pessoa, medico):
        self.data = data
        self.hora = hora
        # há uma diferença grande a seguir: no paciente,
        # vai a 'pessoa inteira', enquanto no médico, 
        # vai só o nome
        self.paciente = pessoa
        self.medico = medico
    def __str__(self):
        # note que para exibir a pessoa em formato texto é preciso 'invocar'
        # a versão textual do atributo paciente (que contém uma pessoa), 
        # usando o método str
        # veja também o \n 'colado' na palavra 'Paciente', 
        # para fazer uma 'quebra de linha' (nova linha)
        return f'Consulta para dia {self.data}, às {self.hora}, \nPaciente: ' +\
        f'{str(self.paciente)}, médico: {self.medico}'

# teste da classe Consulta
nova_consulta = Consulta("01/03/2023", "14:00", nova, "Dr. John Fusacka")
print("*** Teste da classe Consulta:\n", nova_consulta)

'''
resultado da execução:

*** Teste da classe Pessoa:
 
        Nome: João da Silva, 
        Email: josilva@gmail.com, 
        Telefone: 47 91234-5678
        Tipo sanguíneo: O+, 
        Nascido(a) em: 28/10/1988
*** Teste da classe Consulta:
 Consulta para dia 01/03/2023, às 14:00, 
Paciente: 
        Nome: João da Silva, 
        Email: josilva@gmail.com, 
        Telefone: 47 91234-5678
        Tipo sanguíneo: O+, 
        Nascido(a) em: 28/10/1988, médico: Dr. John Fusacka'''