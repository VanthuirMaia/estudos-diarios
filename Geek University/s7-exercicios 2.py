"""
Faça um programa que tenha uma função que recebe uma data no formato string, exemplo: "01/01/2024" e imprima ela por extenso como "1 de janeiro de 2024".
"""

def data_por_extenso(data: str) -> None:
    d = data.split('/')

    dia: int = int(d[0])
    mes: int = int(d[1])
    ano: int = int(d[2])

    if mes == 1:
        mes_str = 'janeiro'
    elif mes == 2:
        mes_str = 'fevereiro'
    elif mes == 3:
        mes_str = 'março'
    elif mes == 4:
        mes_str = 'abril'
    else:
        mes_str = 'desconhecido'

    print(f'{dia} de {mes_str} de {ano}')


if __name__ == '__main__':
    data_por_extenso('01/01/2024')