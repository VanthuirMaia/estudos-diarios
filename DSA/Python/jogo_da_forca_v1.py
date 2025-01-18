"""
    Para desenvolver o jogo da forca em Python, você pode seguir os seguintes passos:


    1- Definir a lista de palavras possíveis

    2- Escolher uma palavra aleatória da lista

    3- Criar uma lista vazia para armazenar as letras adivinhadas

    4- Definir o número máximo de tentativas permitidas

    5- Enquanto o número de tentativas não atingir o limite máximo:

    a. Mostrar a palavra como uma série de underscores, com as letras adivinhadas preenchidas nos espaços corretos

    b. Pedir ao jogador que adivinhe uma letra

    c. Verificar se a letra adivinhada está na palavra

    d. Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra

    e. Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número de tentativas restantes]"

    f. Verificar se todas as letras da palavra foram adivinhadas

    g. Se todas as letras foram adivinhadas, exibir a mensagem "Você venceu!"

    h. Se o número de tentativas restantes chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo.

"""

import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da FORCA")
    print("Advinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['macaco', 'camelo', 'elefante', 'canguru', 'zebra', 'cururu']

    # Escolhe uma palavra aleatoriamente
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para palavras erradas
    letras_erradas = []

    # Loop enquanto o número de chances for maior que zero
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:" " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    
    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

if __name__ == "__main__":
    game()
    print("\nKingston Solutions :)\n")