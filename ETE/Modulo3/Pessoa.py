class Pessoa:
    __nome = str
    def __init__(self, nome):
        self.__nome = nome

p1 = Pessoa('Maria')

print(p1.__nome)