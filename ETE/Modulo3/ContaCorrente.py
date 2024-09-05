from conta import Conta

class ContaCorrente(Conta):

    LIMITE = 5000

    def __init__(self, nome, cpf, email):
        super().__init__()
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__limite_disponivel = self.LIMITE  # Inicializa o limite disponível

    def extrato(self):
        resumo = super().extrato()
        resumo += f'Nome: {self.__nome}\n'
        resumo += f'CPF: {self.__cpf}\n'
        resumo += f'Cheque especial disponível R$: {self.__limite_disponivel}\n'
        return resumo
    
    def juros(self,dias:int):
        return 5000 - self.LIMITE * ((1 + 0.3)**dias)
    
    def saque(self, valor: float):
        saldo_atual = super().saldo()  # Saldo atual da conta

        if saldo_atual >= valor:  # Se o saldo for suficiente, saca do saldo
            super().saque(valor)
            return True
        elif saldo_atual + self.__limite_disponivel >= valor:  # Verifica se o saldo + limite cobre o valor
            valor_restante = valor - saldo_atual
            super().saque(saldo_atual)  # Zera o saldo
            self.__limite_disponivel -= valor_restante  # Deduz o restante do limite
            return True
        else:
            print('Saldo e limite insuficientes.')
            return False

# Exemplo de uso da classe ContaCorrente
conta = ContaCorrente('José', '22345678901', 'teste@teste.com.br')
print(conta.extrato())  # Extrato inicial
conta.depositar(1000)  # Deposita R$ 1000 na conta
print(conta.extrato())  # Mostra o extrato após o depósito
conta.saque(4000)  # Saque R$ 4000, usando saldo e parte do limite
print(conta.extrato())  # Mostra o extrato após o saque
print(conta.juros(1))
