import sqlite3 as db

class Conexao:
    
    def __init__(self):
        self.__conn = db.connect("ETE/Modulo3/projetoADJ/escola.db")
        
    def conect(self):
        return self.__conn
    
    def fechar(self):
        self.__conn.close()