from App.models import DB, _criarListaSQL, _getDate, _getDateTime


class Niveis():
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
        sql = f'SELECT * FROM {self.__Table}'
        sql = DB.readData(sql)
        if sql:
            return _criarListaSQL(sql, self.__class__.__name__ )
    
    def alterar(self, novoNome):
        if self._validarNome(novoNome):
            sql = f'UPDATE {self.__Table} SET Nome = "{novoNome}" WHERE ID = {self.__ID}'
            return DB.queryDB(sql)
    
    def exluir(self):
        pass

