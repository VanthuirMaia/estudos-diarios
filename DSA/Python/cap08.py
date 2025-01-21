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

"""

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
