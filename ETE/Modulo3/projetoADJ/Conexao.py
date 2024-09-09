import sqlite3 as db

class Conexao:
    
    def __init__(self):
        self.__conn = db.connect("escola.db")

    def conect(self):
        return self.__conn