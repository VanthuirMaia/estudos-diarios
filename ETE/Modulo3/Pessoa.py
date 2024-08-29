class Pessoa:
    __nome = str
    def __init__(self):
        pass

        def setNome(self, nome):
            self.__nome = nome
        def getNome(self):
            return self.__nome

p1 = Pessoa()
p1.setNome =("Jose")

print(p1.__nome)