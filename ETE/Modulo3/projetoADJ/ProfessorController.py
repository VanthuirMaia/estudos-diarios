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
                matricula integer not null primary key,
                nome varchar(100) not null,
                email varchar(150) not null
            )
        ''')
        
    def inserir(self,obj:ProfessorModel):
        self.__conn.execute('''
            INSERT INTO aluno (matricula,nome,email) 
            VALUE (?,?,?)''',
            (obj.getMatricula(),obj.getNome(),obj.getEmail(),)
        )