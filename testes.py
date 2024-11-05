class Registro_FUNC:
    def __init__(self, NoFunc, Nome, DataNasc,EstCivil,Endereco,Rg,CIc,Fone,NoDependentes):
        self.NoFunc = NoFunc
        self.Nome = Nome
        self.DataNasc = DataNasc
        self.EstCivil = EstCivil
        self.Endereco = Endereco
        self.Rg = Rg
        self.CIc = CIc
        self.Fone = Fone
        self.NoDependentes = NoDependentes

    def imprimir_dados(self):

        print(f"ID: {self.NoFunc}")
        print(f"Nome: {self.Nome}")
        print(f"Data de nascimento: {self.DataNasc}")
        print(f'Estado Civil: {self.EstCivil}')
        print(f"Endereço: {self.Endereco}")
        print(f"RG: {self.Rg}")
        print(f'CIC: {self.CIc}')
        print(f'Telefone: {self.Fone}')
        print(f'Dependentes: {self.NoDependentes}\n')

funcs = []

def cadastrofunc(n):
    for i in range(n):
        n0 = i+1
        n1 = input("Insira o nome do funcionario: ")
        n2 = input("Insira a data de nascimento: ")
        n3 = input("Insira o estado civil: ")
        n4 = input("Insira o endereço do funcionario: ")
        n5 = input("Insira o RG: ")
        n6 = input("Insira o CIC: ")
        n7 = input("Insira o telefone: ")
        n8 = input("Insira o numero de dependentes: ")
        
        funcionario = Registro_FUNC(n0,n1,n2,n3,n4,n5,n6,n7,n8)
        funcs.append(funcionario)
    i = -1
    while i != 0:
        print("Deseja ver a informação de algum funcionário? \n 1: Sim          0: Não")
        i = int(input())
        if i == 1:
            Id = int(input("Digite o ID do funcionario que deseja vizualizar os dados: "))
            Id -= 1
            funcs[Id].imprimir_dados()

#cadastrofunc(int(input("Insira a quantidade de funcionários que deseja cadastrar: ")))

"""
Exercicio 2
"""
class Autoescola:
    def __init__(self, Nome, Idade, Endereco, Inscricao, Carta):
        self.Nome = Nome
        self.Idade = int(Idade)
        self.Endereco = Endereco
        self.Inscricao = Inscricao
        self.Carta = Carta
    def __str__(self):
        return f"Nome: {self.Nome}, Idade: {self.Idade}, Endereco: {self.Endereco}, Inscricao: {self.Inscricao}, Carta: {self.Carta}"


aluno1 = Autoescola("Gabriel", 18, "Av.Brasil 958", 13022006, 13022025)
aluno2 = Autoescola("Joao", 17, "Av.Brasil 958", 13022006, 13022025)
aluno3 = Autoescola("Pedro", 20, "Av.Brasil 958", 13022006, 13022025)
aluno4 = Autoescola("Gabriel", 20, "Av.Brasil 958", 13022006, 13022025)

alunos = [aluno1,aluno2, aluno3, aluno4]
# Função para encontrar o aluno mais novo e mais velho
def encontrar_alunos_extremos(alunos):
    aluno_mais_novo = []
    aluno_mais_velho = []

    idade_minima = alunos[0].Idade
    idade_maxima = alunos[0].Idade
    # Percorrendo a lista de alunos
    for aluno in alunos:
        if aluno.Idade < idade_minima:
            idade_minima = aluno.Idade
            aluno_mais_novo = [aluno]
        elif aluno.Idade == idade_minima:
            aluno_mais_novo.append(aluno)

        if aluno.Idade > idade_maxima:
            # Novo mais velho encontrado
            idade_maxima = aluno.Idade
            aluno_mais_velho = [aluno]
        elif aluno.Idade == idade_maxima:
            # Adiciona à lista de mais velhos se tiver a mesma idade
            aluno_mais_velho.append(aluno)


    return aluno_mais_novo, aluno_mais_velho
aluno_mais_novo, aluno_mais_velho = encontrar_alunos_extremos(alunos)


print("Alunos mais novos:")
for aluno in aluno_mais_novo:
    print(aluno)

print("\nAlunos mais velhos:")
for aluno in aluno_mais_velho:
    print(aluno)