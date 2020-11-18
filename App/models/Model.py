
from App import Conexao as DB
from datetime import datetime

def getDate():
    return datetime.now().strftime("%d-%m-%Y")

def getDateTime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class User():
    __Table = "USERS"

    def __init__(self, id=None, name='', passw='', lvl='', email='', date=''):
        self.ID = id
        self.name = name
        self.password = passw
        self.level = lvl
        self.email = email
        self.date = date

    def __repr__(self):
        return f'{"id":{self.ID},"name":{self.name},"level":{self.level},"email":{self.email},"date":{self.date} }'
    
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
        cmd =f'SELECT id, name, level, email, date FROM {self.__Table}'
        return DB.readData(cmd)

    def getValues(self):
        values = (self.ID, self.name, self.password, self.level, self.email, self.date)
        return values

       
#x = User()
#print (x.checkLogin())
#print (x.getUserList())
#input('press to continue')

