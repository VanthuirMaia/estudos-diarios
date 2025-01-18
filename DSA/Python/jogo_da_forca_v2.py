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

# Função que desenha a foca na tela
def display_hangman(chances):

    #Lista de estágios da forca
    stages = [ # estágio 6 (final)
               """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
               """,
               # estágio 5
               """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
               """,
               # estágio 4
               """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |      
                    -
               """,
               # estágio 3
               """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |      
                    -
               """,
               # estágio 2
               """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |      
                    -
               """,
               # estágio 1
               """
                    --------
                    |      |
                    |      O
                    |     
                    |     
                    |     
                    -
               """,
               # estágio 0
               """
                    --------
                    |      |
                    |     
                    |     
                    |     
                    |     
                    -
               """
    ]
    return stages[chances]


def game():

    limpa_tela()

    print("\nBem vindo(a) ao jogo da FORCA")
    print("Advinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['macaco', 'camelo', 'elefante', 'canguru', 'zebra', 'cururu']

    # Escolhe uma palavra aleatoriamente
    palavra = random.choice(palavras)

    # lista de letras da palavras
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6

    # Lista para palavras erradas
    letras_tentativa = []

    # Loop enquanto o número de chances for maior que zero
    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        # Tentativa
        tentativa = input("\nDigite uma letra: ")

        # Condicional
        if tentativa in letras_tentativa:
            print("Você já tentou essa letra. Escolha outra!")
            continue
            
        # lista de tentativas
        letras_tentativa.append(tentativa)

        # Condicional
        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")
            
            # Loop
            for indice in range(len(lista_letras_palavras)):
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            # Se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era {}".fotmat(palavra))
                break
        else:
            print("Ops. Essa letra não está na palavra!")
            chances -= 1
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}.".format(palavra))
        

if __name__ == "__main__":
    game()
    print("\nKingston Solutions :)\n")