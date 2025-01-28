"""
# SyntaxError
Ocorre quando o Python encontra um erro de sintaxe, ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.

# NameError
Ocorre quando uma variável ou função não foi definida

# TypeError
Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

# IndexError
Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido

# ValueError
Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto, mas valor inapropriado

# KeyError
Ococrre quando tentamos acessar um dicionário com uma chave que não existe!!!

# AtributeError 
Ocore quando uma variável não tem um atributo/função

# IndentationError
Ocorre quando não respeitamos a indentação do Python (04 espaços)

#################################################################################################

raise TipoDoErro('Mensagem de erro')

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('True', 7)


"""