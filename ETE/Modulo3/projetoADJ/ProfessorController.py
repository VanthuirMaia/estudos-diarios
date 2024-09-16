from Conexao import Conexao

class ProfessorController(Conexao):

    def __init__(self):
        super().__init__()

        self.__conn = Conexao().conect()