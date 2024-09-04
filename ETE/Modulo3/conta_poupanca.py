from conta import Conta
class ContaPoupanca(Conta):

    def __init__(self,nome,cpf):
        super().__init__()
        self.__nome = nome
        self.__cpf = cpf

    def extrato(self):
        resumo = super().extrato()
        resumo += f'Nome:{self.__nome}\n'
        resumo += f'Cpf:{self.__cpf}\n'
        return resumo
    
    def saque(self,valor=float):
        print(super().saldo())

conta = ContaPoupanca('Adjailson','12345678901')
print(conta.extrato())