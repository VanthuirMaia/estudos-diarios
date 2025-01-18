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