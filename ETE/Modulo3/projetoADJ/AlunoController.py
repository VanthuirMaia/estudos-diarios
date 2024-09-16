from Conexao import Conexao


class AlunoController(Conexao):

    def __init__(self):
        super().__init__()
        self.__conn = Conexao().conect()
        self.gerarTabela()


    def gerarTabela(self):
        self.__conn.execute('''
            CREATE TABLE IF NOT EXISTS aluno(
                matricula INTEGER PRIMARY KEY NOT NULL,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL
                                
            )                    
        ''')
        self.fechar()

    def inserir(self,matricula,nome,email):
        self.__conn.execute("INSERT INTO aluno (matricula, nome, email) VALUE (?, ?, ?)",(matricula,nome,email))