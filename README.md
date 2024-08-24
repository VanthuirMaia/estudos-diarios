# estudos-diarios

# Anotações de 30 de Julho de 2024

## O que aprendi hoje

- Conceitos básicos de Python.
	- Funções com Retorno
	- Funções com parâmetro
	- Funções com parâmetro padrão
	- Documentando Funções com Docstrings

- Linguagem SQL para Análise de Dados.
	- Apelidos (AS)

## Recursos utilizados

- [Curso de Python](https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/learn/lecture/11892850#overview).
- [Documentação do Python](https://docs.python.org/pt-br/3/library/functions.html).
- [Artigo sobre Funções](https://medium.com/luizalabs/fun%C3%A7%C3%B5es-em-python-entendendo-par%C3%A2metros-argumentos-args-e-kwargs-4291b1f817f6).
- [Curso de SQL] (https://www.udemy.com/course/curso-completo-sql-para-analise-de-dados/learn/lecture/36512684#overview)

## Reflexões

- Hoje foi um dia produtivo!
- Preciso organizar melhor meu tempo.


# Anotações de 09 de Agosto de 2024
- Conceitos básicos Django.
	- Criando um projeto web
	- Separando as páginas
	
# Após um fds de trabalho, hoje foi dia de estudar Flutter e Django

# Anotações 16/08/2024
	- Criando a classe Evento

		# Classe Evento em Python

				Este repositório contém uma implementação simples de uma classe Python chamada `Evento`, que representa um evento com um nome e um local. A classe inclui métodos para imprimir informações do evento, criar eventos online e calcular o número máximo de pessoas que podem caber em uma determinada área.

				## Estrutura da Classe

				### 1. `__init__(self, nome, local="")`
				O construtor inicializa uma nova instância de `Evento` com os seguintes parâmetros:
				- `nome`: O nome do evento.
				- `local`: O local do evento (opcional, padrão é uma string vazia).

				### 2. `imprime_informacoes(self)`
				Este método imprime o nome e o local do evento no console.

				### 3. `@classmethod cria_evento_online(cls, nome)`
				Este método de classe cria um evento online com uma URL de local pré-definida. Ele retorna uma nova instância da classe `Evento` com o nome especificado e o local como um link online.

				### 4. `@staticmethod caucula_limite_pessoas_area(area)`
				Este método estático calcula o número máximo de pessoas que podem caber em uma determinada área. O método funciona da seguinte maneira:
				- Para áreas entre 5 e 10 metros quadrados, retorna 5 pessoas.
				- Para áreas entre 10 e 20 metros quadrados, retorna 15 pessoas.
				- Para áreas maiores ou iguais a 20 metros quadrados, retorna 30 pessoas.
				- Para áreas menores que 5 metros quadrados, retorna 0 pessoas.

				## Exemplo de Uso

				```python
				# Criação de eventos
				ev = Evento("Aula de Python")
				ev2 = Evento("Aula de JS", "Rio de Janeiro")

				# Criação de evento online
				ev_online = Evento.cria_evento_online("Live de Python")

				# Impressão das informações do evento
				ev2.imprime_informacoes()

				# Cálculo do limite de pessoas
				print(Evento.caucula_limite_pessoas_area(5))  # Saída: 5


# Estudando POO - Programação Oreintada a objetos
	Parei no vídeo: 32

# Anotações 23/08/2024
	# Estudando POO - Programação Orientada a Objetos
		Atributo de classe e f-strings
		Herança 
		Importando módulos
		Revisão de protocolos HTTP