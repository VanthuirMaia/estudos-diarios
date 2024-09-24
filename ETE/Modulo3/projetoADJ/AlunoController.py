from Conexao import Conexao
from AlunoModel import AlunoModel

class AlunoController(Conexao):
    
    def __init__(self, view):
        self.view = view
        super().__init__()
        self.__conn = Conexao().conect()
        self.gerarTabela()

    def gerarTabela(self):
        self.__conn.execute('''
            CREATE TABLE IF NOT EXISTS aluno(
                matricula integer not null primary key,
                nome varchar(100) not null,
                email varchar(150) not null
            )
        ''')
        self.fechar()

    def inserir(self):
        matricula = int(self.view.matricula.get())
        nome = self.view.nome.get()
        email = self.view.email.get()
        obj = AlunoModel()
        obj.setMatricula(matricula)
        obj.setNome(nome)
        obj.setEmail(email)
        try:
            self.__conn.execute("INSERT INTO aluno (matricula,nome,email) VALUES (?,?,?)", (obj.getMatricula(), obj.getNome(), obj.getEmail()))
            self.__conn.commit()
            return True
        except:
            return False

    def excluir(self):
        matricula = int(self.view.matricula.get())
        try:
            self.__conn.execute("DELETE FROM aluno WHERE matricula = ?", (matricula,))
            self.__conn.commit()
            return True
        except:
            return False

    def atualizar(self):
        matricula = int(self.view.matricula.get())
        nome = self.view.nome.get()
        email = self.view.email.get()
        
        try:
            self.__conn.execute("UPDATE aluno SET nome = ?, email = ? WHERE matricula = ?", (nome, email, matricula))
            self.__conn.commit()
            return True
        except Exception as e:
            return False
        