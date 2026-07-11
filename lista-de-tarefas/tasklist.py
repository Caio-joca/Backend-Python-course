class Tasklist :
    def __init__(self, lista):
        self.lista = lista
    def listviewer (self) :
        howmany = len(self.lista)
        for i in range(howmany) :
            for a in self.lista :
                print(f'nome:{a.nome} condição:{a.condition}')