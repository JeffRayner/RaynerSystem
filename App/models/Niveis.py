from App import Conexao as DB

class Nivel():
    __Table= "NIVEIS"

    def __init__(self, ID=None, Nome=""):
        self.__ID = ID
        self.__Nome = Nome

    def __repr__(self):
        return f'{self.__class__.__name__}(ID={self.__ID}, Nome="{self.__Nome}")'

    def __str__(self):
        return f'ID: {self.__ID}\nNome: {self.__Nome}'

    def getValues(self):
        return {"id":self.__ID, "nome":self.__Nome}

    def _validarNome(self, Nome):
        return len(Nome) >= 3

    def cadastrar(self):
        if self._validarNome(self.__Nome):
            sql = f'INSERT INTO {self.__Table} (Nome) VALUES ("{self.__Nome}")'
            return DB.queryDB(sql)
    
    def listar(self):
        lista = []
        sql = f'SELECT * FROM {self.__Table}'
        sql = DB.readData(sql)
        if sql:
            for i in sql:
                i = Nivel(*i)
                lista.append(i.getValues())
            return lista
    

