"""
Crie um programa que tenha uma função que recebe um parãmetro inteiro e devolve seu dobro
"""


def dobro(numero: int) -> int:
    return numero * 2

if __name__ == '__main__':
    valor: int = 4
    print(f'O dobro de {valor} é {dobro(valor)}')