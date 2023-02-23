# a classe Pessoa vai conter os dados que
# são comuns às classes Paciente e Medico
class Pessoa:
    def __init__(self, nome, email, dt_nasc):
        self.nome = nome
        self.email = email
        self.data_nascimento= dt_nasc
    def __str__(self): 
        return f'''
        Nome: {self.nome}, 
        Email: {self.email}, 
        Nascido(a) em: {self.data_nascimento}'''

# definição da classe Paciente
# o paciente é uma pessoa, com mais 2 atributos :-)
class Paciente(Pessoa):
    def __init__(self, nome, email, dt_nasc, telefone, tps):
        super().__init__(nome, email, dt_nasc)
        self.telefone = telefone
        self.tipo_sanguineo = tps
    def __str__(self):
        return f'''
        {super().__str__()},
        Contato: {self.telefone}, 
        Tipo sanguíneo: {self.tipo_sanguineo}
        '''

# teste do paciente
nome = "João da Silva"
email = "josilva@gmail.com"
nasc = "28/10/1988"
telefone = "47 91234-5678"
tipo_sang = "O+"
# criar o paciente
novo_paciente = Paciente(nome, email, nasc, telefone, tipo_sang)
# exibir os dados
print("*** Teste da classe Paciente:\n", novo_paciente)

# classe Medico
# o médico também é uma pessoa :-)
class Medico(Pessoa):
    def __init__(self, nome, email, dt_nasc, crm, espec):
        super().__init__(nome, email, dt_nasc)
        self.CRM = crm
        self.especialidade = espec
    def __str__(self):
        return f'''
        {super().__str__()},
        CRM: {self.CRM}, 
        Especialidade: {self.especialidade}
        '''

# teste da classe Medico
nome = "Dr. John Fusacka"
email = "jofusacka@gmail.com"
tipo_sang = "AB-"
numero_crm = "123ABC-9"
residencia = "Homeopatia"
# criar o médico
novo_medico = Medico(nome, email, nasc, numero_crm, residencia)
# exibir os dados
print("*** Teste da classe Medico:\n", novo_medico)

class Consulta:
    def __init__(self, data, hora, paciente, medico):
        self.data = data
        self.hora = hora
        self.paciente = paciente
        self.medico = medico
    def __str__(self):
        return f'''Consulta para dia {self.data}, às {self.hora},
        Paciente: {str(self.paciente)}
        Médico: {str(self.medico)}'''

# teste da classe Consulta
nova_consulta = Consulta("01/03/2023", "14:00", novo_paciente, novo_medico)
print("*** Teste da classe Consulta:\n", nova_consulta)

'''
resultado da execução:

*** Teste da classe Paciente:
 
        
        Nome: João da Silva, 
        Email: josilva@gmail.com, 
        Nascido(a) em: 28/10/1988,
        Contato: 47 91234-5678, 
        Tipo sanguíneo: O+
        
*** Teste da classe Medico:
 
        
        Nome: Dr. John Fusacka, 
        Email: jofusacka@gmail.com, 
        Nascido(a) em: 28/10/1988,
        CRM: 123ABC-9, 
        Especialidade: Homeopatia
        
*** Teste da classe Consulta:
 Consulta para dia 01/03/2023, às 14:00,
        Paciente: 
        
        Nome: João da Silva, 
        Email: josilva@gmail.com, 
        Nascido(a) em: 28/10/1988,
        Contato: 47 91234-5678, 
        Tipo sanguíneo: O+
        
        Médico: 
        
        Nome: Dr. John Fusacka, 
        Email: jofusacka@gmail.com, 
        Nascido(a) em: 28/10/1988,
        CRM: 123ABC-9, 
        Especialidade: Homeopatia
        
'''