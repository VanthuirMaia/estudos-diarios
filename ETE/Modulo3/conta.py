import random as r

class Conta:
    AGENCIA = '3212'

    def __init__(self):
        self.__numero = r.randint(111111, 999999)
        self.__saldo = 0

    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor=float):
        self.__saldo += valor
    
    def extrato(self):
        resumo = f'Agência:{self.AGENCIA}\n'
        resumo += f'Número:{self.__numero}\n'
        resumo += f'Saldo R$:{self.saldo()}\n'
        return resumo

conta = Conta()
print(conta.AGENCIA )
conta.depositar(105)
print(conta.extrato())