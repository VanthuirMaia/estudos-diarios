from Conexao import Conexao
from ProfessorModel import ProfessorModel
class ProfessorController(Conexao):

    def __init__(self):
        super().__init__()

        self.__conn = Conexao().conect()
        self.gerarTabela()

    def gerarTabela(self):
        self.__conn.execute('''
            CREATE TABLE IF NOT EXISTS professor(
                matricula INTEGER PRIMARY KEY NOT NULL,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL                      
            )
''')
        
        def inserir(self,obj:ProfessorModel):
            self.__conn.execute("INSERT INTO aluno (matricula, nome, email) VALUE (?, ?, ?)",(obj.getMatricula(),obj.getNome(),obj.getEmail(),))