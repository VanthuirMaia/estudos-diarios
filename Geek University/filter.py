"""
Filter - serve para filtrar dados de uma determinada coleção

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Cauculando a média dos dados usando a função "mean()" - É uma função da biblioteca statistcs
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map, após serem utilizados os dados de filter, eles são excluidos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

# res = filter(None, paises)

# print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

"""

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

# Filtrar os usuarios que estão inativos no Twitter

print(usuarios)

# Verifica se na chave 'tweets' a quantidade (len) é igual a zero, se for ele coloca na lista
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

print(f"A quantidade de usuários inativos é {len(inativos)} e os usuários inativos são: {[u['username'] for u in inativos]}")
