# Exemplo básico de Python de herança

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        Pessoa.__init__(self, nome, idade)
        self.curso = curso

    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        Pessoa.__init__(self, nome, idade)
        self.salario = salario

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

class Coordenador(Professor):
    def __init__(self, nome, idade, salario, curso):
        Professor.__init__(self, nome, idade, salario)
        self.curso = curso

    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso

pessoa = Pessoa("João", 20)
aluno = Aluno("Maria", 25, "Sistemas de Informação")
professor = Professor("José", 30, 1000)
coordenador = Coordenador("Ana", 35, 2000, "Sistemas de Informação")

print("Nome Pessoa: " + pessoa.getNome())
print("Idade: " + str(pessoa.getIdade()))
print("Nome Aluno: " + aluno.getNome())
print("Idade: " + str(aluno.getIdade()))

print("Nome Professor: " + professor.getNome())
print("Idade: " + str(professor.getIdade()))
print("Salário: " + str(professor.getSalario()))

print("Nome Coordenador: " + coordenador.getNome())
print("Idade: " + str(coordenador.getIdade()))
print("Salário: " + str(coordenador.getSalario()))
print("Curso: " + coordenador.getCurso())

coordenador.setCurso("Engenharia de Software")
print("Alteração do Curso: " + coordenador.getCurso())

# Fim do arquivo heranca_ex1.py
