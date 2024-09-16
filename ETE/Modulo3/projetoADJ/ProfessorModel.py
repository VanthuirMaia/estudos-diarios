
class ProfessorModel:
    __matricula = int
    __nome = str
    __email = str

    def setMatricula(self, matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
    
    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome

    def setEmail(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email
    
    def toMaps(self):
        return {
                'matricula':self.getMatricula(),
                'nome':self.getNome(),
                'email':self.getEmail()
                  }