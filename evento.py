class Evento:
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
                             
    def imprime_informacoes(self):
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)

    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local="https://tamarcado.com/eventos?id=1")
        return evento
    
    @staticmethod
    def caucula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
                     
ev = Evento("Aula de Python")
ev2 = Evento("Aula de JS", "Rio de Janeiro")
             
ev_online = Evento.cria_evento_online("Live de Python")
# ev2.imprime_informacoes()

print(Evento.caucula_limite_pessoas_area(5))