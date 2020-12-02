from App.models import DB, _criarListaSQL, _getDate, _getDateTime

class User():
    __Table = "USERS"

    def __init__(self, id=None, name='', passw='', lvl=None, email='', date=''):
        self.id = id
        self.name = name
        self.password = passw
        self.level = lvl
        self.email = email
        self.date = date
    
    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, name="{self.name}", passw="", lvl={self.level}, email="{self.email}", date="{self.date}")'

    def __str__(self):
        return f'ID: {self.id}\nName: {self.name}\nLevel: {self.level}\nEmail: {self.email}\nDate:{self.date}'

    def getDictValues(self):
        return {"id":self.id, "name":self.name, "lvl":self.level, "email":self.email, "date":self.date}

    def __clearPassword(self):
        self.password = ''
    
    def creatUser(self):
        self.date = _getDate()
        sql = f'INSERT INTO {self.__Table} (name, password, level, email, date) VALUES ("{self.name}","{self.password}",{self.level},"{self.email}","{self.date}")'
        return DB.queryDB(sql)
    
    def checkLogin(self):
        sql = f'SELECT * FROM {self.__Table} WHERE name = "{self.name}" AND password = "{self.password}" '
        sql = DB.readData(sql, True)
        if sql:
            self.__init__(*sql)
            self.__clearPassword()
            return True
    
    def changePassword(self, newPassword):
        sql = f''
        return DB.queryDB(sql)

    def changeLevel(self, newLvl):
        sql = f''
        return DB.queryDB(sql)

    def getUserList(self):
        listaDeUsuarios = []
        sql =f'SELECT * FROM {self.__Table}'
        sql = DB.readData(sql)
        if sql:
            for usuario in sql:
                usuario = User(*usuario)
                listaDeUsuarios.append( usuario.getDictValues())
            return listaDeUsuarios


