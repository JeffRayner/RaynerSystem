from App import Conexao as DB
from datetime import datetime

def getDate():
    return datetime.now().strftime("%d-%m-%Y")

def getDateTime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class User():
    __Table = "USERS"

    def __init__(self, id=None, name='', passw='', lvl='', email='', date=''):
        self.id = id
        self.name = name
        self.password = passw
        self.level = lvl
        self.email = email
        self.date = date
    
    def __repr__(self):
        return f'{{ "id":{self.id}, "name":"{self.name}", "level":{self.level}, "email":"{self.email}", "date":"{self.date}" }}'

    def __clearPassword(self):
        self.password = ''
    
    def creatUser(self):
        self.date = getDate()
        cmd = f'INSERT INTO {self.__Table} (name, password, level, email, date) VALUES ("{self.name}","{self.password}",{self.level},"{self.email}","{self.date}")'
        return DB.queryDB(cmd)
    
    def checkLogin(self):
        cmd = f'SELECT * FROM {self.__Table} WHERE name = "{self.name}" AND password = "{self.password}" '
        res = DB.readData(cmd, True)
        if res:
            self.__init__(*res)
            self.__clearPassword()
            return True

    def getUserList(self):
        users = []
        cmd =f'SELECT * FROM {self.__Table}'
        cmd = DB.readData(cmd)
        for u in cmd:
            users.append( eval(str(User(*u))) )
        return users

    def getValues(self):
        values = (self.id, self.name, self.password, self.level, self.email, self.date)
        return values

       
#x = User()
#l = x.getUserList()
#print ( type(l[0]) )