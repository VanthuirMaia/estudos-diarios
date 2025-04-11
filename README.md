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

# Anotações 25/08/2024

    # Estudando POO - Programação Orientada a Objetos
    	# Geek University
    		Tipos de Paradigma (Estruturada, Funcional, POO)
    		Conteúdo: Classes
    		Conteúdo: Atributos
    			Atributos de Instância
    			Atributos de classe
    			Atributos Dinâmicos

# Anotações 03/09/2024

    # Reiniciando o curso de Django

# Anotações 04/09/2024

    #ETE - Funções

# Anotações 25/09/2024

    # Iniciando treinamento de Delphi
    	Criando um Sistema de vendas
    		* Tela principal
    		* Menu
    		* Footer

# Anotações 26/09/2024

    # Iniciando a construção do Dashboar Miroute
    	Criando o projeto Django - Miroute
    	Criando a rota e templates Dashboard
    	Utilizando Bootstrap

# Anotações 02/10/2024

    # Reiniciando os estudos de DRF

# Anotações 02/10/2024

    # Miroute
    	Hoje foi dia de trabalhar no Miroute. Desenvolvi a tela adm principal, com Navbar, Sections de Cards de links, Dashboard, Mapa e Seção de produtos.
    	Foi um grane desafio, fazer tudo isso em tão pouco tempo, mas o resultado foi satisfatório!!!

# Anotações 01/01/2025

Iniciando o projeto 365 dias programando

Hoje comecei a ver um curso sobre Docker.
Iniciei um projeto pessoal de uma aplicação para automatizar envios de mensagens via whatsapp.
Me matriculei em um curso sobre DevOps e AWS.

# Anotações 02/01/2025

Continuando o curso de Docker, identifiquei possíveis incosistências nas tecnologias escolhidas para o projeto WhatsPlus.
Vou avaliar a possibilidade de alterar as tecnologias... Laravel ou Spring
Ja em busca de um curso sobre!!!

# Anotações 03/01/2025

Até agora, sucesso nos estudos em 2025. Apesar da viagem de + 600 km, + de 10hs dirigindo, ainda deu tempo de ver o curso de Docker, ao menos superficial.
Consegui entender um pouco sobre Mapeamento de portas, attach, exec...
Ainda ta no início, mas ja consigo começar a entender os conceitos.

# Anotações 04/01/2025

Reiniciando o curso de Desenvolvimento Web, basicamente reiniciando a seção JavaScript.
_ Aprendendo sobre a precedência de execução (Citado o DOM)
_ Comentários em códigos
_ Variáveis (tipos, regras para declaração)
_ Comandos de visualização (alert, document.write, console.log)
_ Concatenação
_ Valores "Null" e "Undefined" \* Alterando valores das variáveis

    *Foi proposto um desafio, para serem declaradas 3 variaveis, mostradas através de um document.write, depois disso serem alteradas usando lógica.

    			Desafio realizado com sucesso

    * Iniciando If / Else
    * Operadores de comparação
    * Desafio de criação de uma lógica para verificar média de alunos usando If e Else, incrementei um pouco mais e coloquei também um Else If.
    			Desafio realizado com sucesso

# Anotações 05/01/2025

    Dia pouco produtivo, mas ainda possível de estudar!!!
    	Vi alguns conteúdos sobre MicroSaas e também estudei Inglês.
    	#Seguimos

# Anotações 06/01/2025

    Iniciando os estudos de hoje, com a live sobre DevOps e Cloud.
    	Conceitos interessantes que eu ja pretendia aprender
    Segunda parte dos estudos de  hoje, iniciei um curso avançado de React. Pretendo usar em meu projeto WhatsPlus, por isso a escolha por essa stack.
    	NextJS
    		* SSR (Renderização no Servidor (Server Side Rendering))
    		* SSG (Geração de Estáticos (Static Site Generation))
    		* CSS-in-JS (Styled-jsx, Styled Components, Emotion, etc)
    		* Zero Configuration (rotas, hot reloading, code splitting...)
    	Tipos de aplicação
    		# Static Site (HTML/CSS/JS) - GatsbyJS, Hexo
    		# Client Side Rendering (Single Page Application - SPA) - Create React APP
    		# Server Side Rendering (SSR) - NextJS
    	GraphQL
    		Diferenças entre REST API x GraphQL
    	GraphQL Client
    		Bibliotecas
    			FetchQL
    			GraphQL-request
    			uRQL
    			RelayModern
    			Apollo Client

# Anotações 07/01/2025

    WSL / Docker e VSCode (Imersão em DevOps e Cloud)

# Anotações 08/01/2025

    Hoje resolvi voltar ao começo. Repensar minha stack, e o que eu quero para o futuro.
    Voltando ao curso de Python, do básico ao avançado - Geek University
    	Relembrando tópicos importantes de funções.
    		- Funções com parâmetro
    		- Funções com parãmetro padrão
    	Documentando funções com docstrings
    	Entendendo o parâmetro *args (comparado a uma LISTA)
    		- Desempacotador (* )
    	Entendendo o parâmetro **kwargs (comparado a um DICIONARIO)
    		- Desempacotador (** )
    	Entendendo a importância de manter a ordem dos parãmetros na declaração

    Intercalando com o curso de desenvolvimento Web. A partir de agora, estudando JS
    	Trabalhando o casting de dados
    	Operadores Logicos

    Atividade de uso dos operadores lógicos realizada com sucesso, na primeira tentativa.

    # Anotações 09/01/2025
    	Introdução ao Power BI psrs Business Intenligence e Data Science

    # Anotações 10/01/2025
    	Power BI
    		Power Query
    		Visuais
    		Opções e Configurações
    	Criando um dashboard inicial com um dataset de dados de vendas
    		Incrível como o PowerBI facilita a vida dos analistas. Continuarei me especializando, pra quando a oportunidade aparecer, estar pronto.

    # Anotações 11/01/2025
    	Power BI
    		Iniciando a Modelagem de dados
    			Formas de aplicação e benefícios
    		DAX
    		Linguagem "M"
    	Criando mais um Dashboard interativo, com métricas de Vendas, Custo, Margem de Lucro e KPI

    # Anotações 12/01/2025
    	Revisão do conteúdo estudado durante a semana

    # Anotações 13/01/2025
    	Curso de Python
    		List Comprehension
    		Listas Aninhadas
    		Dictionary Comprehension
    		Set Comprehension

    # Anotações 14/01/2025
    	Power BI
    		Ralizando análises na área de marketing
    			Segmentação
    			Outliers
    			Medidas
    			Árvore Hierárquica

    # Anotações 15/01/2025
    	Power BI
    		Projeto de Análise de Trabalho de Marketing
    			Paginação
    			Tabelas
    			Matriz
    	Python
    		Expressões Lambdas
    			Bônus: Usando strip, title, Split, lower, upper, sort

    # Anotações 16/01/2025
    	Power BI
    		Finalizando Projeto de Análise de Trabalho de Marketing
    			Formatando e alinhando detalhes de exibição
    			Narrativa Inteligente
    			Principais Influenciadores

    # Anotações 17/01/2025
    	Power BI
    		Finalizando Projeto de Análise de Trabalho de Marketing
    			Faltando apenas criar o índice
    	Python para Análise de dados
    		Treinando os fundamentos de Python, criando um jogo simples (Forca)
    		Treinando os fundamentos de Python, criando um jogo v2 simples com caracters com imagem (Forca)
    		Programação Orientada a Objetos

    # Anotações 18/01/2025
    	SQL
    		Hoje o estudo foi sobre SQL, assistindo as aulas do curso de SQL para Análise de dados
    			Subconjuntos da linguagem
    			Dialetos
    			Iniciando no Google BigQuery
    			Comandos de seleção

    # Anotações 19/01/2025
    	Revisão do conteúdo estudado durante a semana
    		Python, PowerBI, SQL e Python para Análise de dados

    # Anotações 20/01/2025
    	Power BI
    		Criação de índice
    			Formatação final do relatório
    	Python para Análise de dados
    		Class
    			Atributos
    			Objetos
    			Manipulando atributos
    				hasattr / setattr / getattr / delattr

    # Anotações 21/01/2025
    	Python - Fundamentos
    		Map
    		Filter
    		Biblioteca (statistcs)
    			Função mean
    		Removendo dados faltantes com Filter
    		Atividade (Analisar ususarios e tweets)
    		Reduce (Melhor usar um loop "for ou While")
    		Any e All

    # Anotações 22/01/2025
    	Python - Fundamentos (Funções Integradas)
    		Generators Expression
    			Diferenças entres ele e List, Set e Dict Comprehension (Ocupa menos espaço de memória)
    		Sorted
    		Min e Max
    		Reversed
    		Len, Abs, Sum e Round
    		Zip
    # Anotações 23/01/2025
    	Power BI
    		Iniciando projeto de RH
    # Anotações 24/01/2025
    	Power BI
    		Continução do projeto RH
    # Anotações 25/01/2025
    	Power BI (Final de semana complicado pra estudar, tempo, cansaço, mas fiz o meu melhor)
    		Projeto RH
    			Medidas DAX COUNTROWS / AVERAGE / DIVIDE
    			Coluna condicional
    			Medidas com DAX a partir da coluna condicional
    # Anotações 26/01/2025
    	Power BI
    		Continução do projeto RH

    # Anotações 27/01/2025
    	Power BI
    		Finalização do projeto RH
    			Visualmente, com medidas formatadas e salvas, Dashboard pronto para o uso.
    	Python - Debugando e Tratando erros
    		Erros mais comuns
    		Levantamento de erros usando "Raise"

    # Anotações 28/01/2025
    	Power BI
    		Iniciando Projeto Logística
    			Avaliando Dashboard e sugerindo possíveis alterações e correções.

    # Anotações 29/01/2025
    	Power BI
    		Finalizado Projeto Logística
    			Correções no Dashboard realizadas (Alterado modelos, graficos e organização dos dados)

    # Anotações 30/01/2025
    	Python para Análise de dados
    		Manipulando atributos
    			has attr
    			set attr
    			get attr
    			del attr
    		Criando um jogo usando POO (Forca)
    		NUMPY
    			Indexação

    # Anotações 31/01/2025
    	Python para Análise de dados
    		Numpy
    			Funções Numpy
    			Manipulando Matrizes
    			Manipulando Objetos de 3 e 4 dimensões
    			Manipulando Arquivos

    # Anotações 01/02/2025
    	Python para Análise de dados
    		Numpy
    			Manipulando Arquivos

    # Anotações 02/02/2025
    	Power BI
    		Iniciando Projeto da Área de Finanças Empresarial

    # Anotações 03/02/2025
    	Power BI
    		Projeto Finanças
    			Carregando dados XLS e analisando erros
    			Realizando Pivot da tabela
    			Criando Hierarquia de Datas
    			Criando medidas com indicadores
    		Projeto Finalizado

    # Anotações 04/02/2025
    	Python para Análise de dados
    		Manipulação de arquivos usando o Numpy
    		Manipulando um arquivo csv, removendo linhas e colunas desnecessárias (Usecols, skiprows)
    		Iniciando em Análise Estátistica
    			Média (mean)
    			Desvio Padrão (std)
    			Variância (var)
    		Operações Matemáticas
    			Soma (sum)
    			Soma Acumulada (cumsum)
    			Produto (prod)
    			Multiplicação (dot) ou simplismente "@"
    	Flask
    		Iniciei a criação de um site para Portfolio
    			Criei do zero usando Flask, HTML, CSS e Bootstrap
    			Templates criados (Home, Projetos, Sobre e Contato)
    			Formulário de contato funcionando

    # Anotações 05/02/2025
    	Power BI
    		Iniciando Projeto da Área Contábil

    # Anotações 06/02/2025
    	Python para Análise de dados
    		NumPy
    			Slicing
    			Flatten
    			Repeat
    			Tile
    			Copy
    		Pandas - Introdução
    			Head
    			Manipulando dados com o Pandas

    # Anotações 07/02/2025
    	Python - Análise e Engenharia de Dados (Youtube)
    		Jornada de Dados (Luciano Galvão Filho)
    		Iniciando um Projeto de ETL com Python

    # Anotações 08/02/2025
    	SQL - Workshop de SQL com Databrics
    		Comandos Select, From, Count, Distinct
    			Where, Limit, Order By, Min, Max, Sum, Avg
    			Group By, Having, Join (Inner, Left e Right)
    			Subquery, CTE, View e Tabelas
    # Anotações 09/02/2025
    	Revisão do conteúdo visto durante a semana
    # Anotações 10/02/2025
    	Python - Análise e Engenharia de Dados (Youtube)
    		Web Scraping com Python / AWS / Azzure
    # Anotações 11/02/2025
    	Lakehouse com Arquitetura Medalhão no Databricks
    # Anotações 12/02/2025
    	Power BI - Retornando ao Projeto - Balanço Patrimonial
    # Anotações 13/02/2025
    	Power BI - Finalizando Projeto - Balanço Patrimonial
    # Anotações 14/02/2025
    	Power BI - Finalizando Projeto - Balanço Patrimonial
    # Anotações 15/02/2025
    	Preditiva ai - Introdução ao Mundo dos dados
    # Anotações 16/02/2025
    	Power BI - Projeto - Balanço Patrimonial
    # Anotações 17/02/2025
    	Power BI - Projeto Finalizado - Balanço Patrimonial
    	Storitelling com dados
    	Power BI - Projeto - Análise de Ações
    # Anotações 18/02/2025
    	Python - SQL - Databricks
    		Criando uma ETL, acessando dados SQL e CSV, e elaborando um  Dashboard
    # Anotações 19/02/2025
    	Desenvolvimento do Site (Portifolio) - 30% pronto
    # Anotações 20/02/2025
    	Desenvolvimento do Site (Portifolio) - 50% pronto
    # Anotações 21/02/2025
    	Power BI - Projeto Análise de Ações do Mercado Financeiro
    # Anotações 22/02/2025
    	Projeto da Especialização UFRPE - Desenvolver um Relatório Executivo com Dashboard.
    	Power BI - Tratamento de dados
    # Anotações 23/02/2025
    	Power BI - Tratamento de dados, Análise exploratória, Análise Estatística
    # Anotações 24/02/2025
    	Power BI - Limpeza e Manipulação de Dados
    	Power Query - Linguagem M
    # Anotações 25/02/2025
    	Iniciando na Jornada de dados - Focando Data Engineer
    # Anotações 26/02/2025
    	Elaborando Análise e Dashboard para o MiRoute - Commit retroativo
    # Anotações 27/02/2025
    	Jornada de dados - Github (Treinamento)
    # Anotações 28/02/2025
    	Jornada de dados - Bootcamp Python Aula 01 (Python, Git e VSCode)
    # Anotações 01/03/2025
    	Jornada de dados - Bootcamp Python Aula 02 (TypeError, Type Check, Type Conversion, Try-Except e If)
    # Anotações 02/03/2025
    	Jornada de dados - Bootcamp Python Aula 02 (TypeError, Type Check, Type Conversion, Try-Except e If)
    # Anotações 03/03/2025
    	Jornada de dados - Bootcamp Python Aula 03 (Debug, If, For, While, Listas e Dicionários)
    # Anotações 09/03/2025
    	Revisão do conteúdo visto essa semana
    		Python - Funções
    		Criação de ETLL - Pipeline
    # Anotações 10/03/2025
    	Revisão do Picth - MiRoute
    # Anotações 11/03/2025
    	Revendo aula 09 do Bootcamp Python - Sanar dúvidas sobre decoradores
    # Anotações 12/03/2025
    	POO - Aula 01
    # Anotações 13/03/2025
    	POO - Aula 02
    # Anotações 14/03/2025
    	POO - Aula 03 - Herança
    # Anotações 15/03/2025
    	POO - Continuação da Aula 03 - Polimorfismo
    # Anotações 16/03/2025
    	POO - Revisão do conteúdo visto na semana
    # Anotações 17/03/2025
    	Realizando Análise e Criaçãod e Dashboard para apresentação de Seminários
    # Anotações 19/03/2025
    	Finalizando apresentação do Seminários - Pós (Especialização TDBE - UFRPE)
    # Anotações 20/03/2025
    	Finalizando apresentação do Seminários - Pós (Especialização TDBE - UFRPE)
    # Anotações 21/03/2025
    	Trabalhando com Desenvolvimento Web - Desenvolvendo meu portifólio em Django
    # Anotações 22/03/2025
    	Jornada de Dados - CRUD / SQLModel
    # Anotações 23/03/2025
    	Revisão do conteúdo visto na semana
    # Anotações 25/03/2025
    	SQLAlchemy
    # Anotações 27/03/2025
    	SQLAlchemy (Continuação)
    # Anotações 28/03/2025
    	CRUD - API
    # Anotações 30/03/2025
    	CRUD - API - Continuação
    # Anotações 31/03/2025
    	Finalizado Projeto CRUD - FastAPI
    # Anotações 01/04/2025
    	Iniciando Bootcamp SQL
    # Anotações 02/04/2025
    	Bootcamp SQL - 3ª aula
    # Anotações 03/04/2025
    	Resolvendo BUG de uma aplicação Python
    # Anotações 04/04/2025
    	Bootcamp SQL - 4ª aula
    # Anotações 05/04/2025
    	Revisão SQL
    # Anotações 06/04/2025
    	Revisão SQL
    # Anotações 07/04/2025
    	Window Function
    	Os últimos commit estão sendo únicos pr dia, devido ao fato dos estudos estarem centralizados no PG Admin
    # Anotações 07/04/2025
    	Window Function - Revendo a aula jovamente, devido a dificuldade com os comandos.
    # Anotações 10/04/2025
    	Workshop Ai Agents
    # Anotações 11/04/2025
    	Projeto SQL - Bootcamp SQL
