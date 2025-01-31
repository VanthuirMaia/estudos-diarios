"""
# Criando uma classe chamada Livro
class Livro():
    def __init__(self):
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print('Construtor chamado para criar um objeto desta classe.')
    
    def imprime(self):
        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))

# Criando uma instância da classe Livro
Livro1 = Livro()

Livro1.titulo

Livro1.imprime()

# Criando uma classe chamada Livro
class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto desta classe.')
    
    def imprime(self, titulo, isbn):
        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))

# Criando uma instância da classe Livro
Livro2 = Livro("O Poder do Hábito", 77886611)

Livro2.titulo

Livro2.imprime("O Poder do Hábito", 77886611)

class Algoritmo():

    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")
# Criando objetos a partir da classe
algo1 = Algoritmo(tipo_algo='Random Forest')
algo2 = Algoritmo(tipo_algo='Deep Learning')

# Atributos da classe
algo1.tipo
algo2.tipo

"""
# Criando uma classe
class Funcionarios:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print("Funcionario(a) " + self.nome + " tem salário de R$ " + str(self.salario) + " e o cargo é " + self.cargo)

# Ciando um objeto chamado Func1 a partir da classe funcionarios
Func1 = Funcionarios("Mary", 20000, "Cientista de Dados")

# Usando o método da classe
Func1.listFunc()


print("**** Usando atributos ****")
hasattr(Func1, "nome")
hasattr(Func1, "salario")
setattr(Func1, "salario", 4500)
hasattr(Func1, "salario")
getattr(Func1, "salario")
delattr(Func1, "salario")
hasattr(Func1, "salario")