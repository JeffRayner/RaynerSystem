from App import con1 as DB
from secrets import token_urlsafe
#print(token_urlsafe(4)) #gerar token

class Profile():
    __Table= "PROFILE"

    def __init__(self, ID=None, url="", name="", title="", email=""):
        self.__ID = ID
        self.__url = url
        self.name = name
        self.title = title
        self.email = email

    @property
    def id(self):
        return self.__ID

    @property
    def url(self):
        return self.__url

    def getValues(self) :
        return {"id":self.__ID, "url":self.__url, "nome":self.name, \
            "title":self.title, "email":self.email}

    def generateUrl(self):
        self.__url = token_urlsafe(4)

    def create(self):
        self.generateUrl()
        sql = f'INSET INTO {self.__Table} (url, name, title, email) VALUES (?, ?, ?, ?)'
        values = (self.__url, self.name, self.title, self.email)
        #print(sql)
        #return DB.queryDB(sql, values)


    def getUsuario(self, url: str):
        resultado = Profile()
        cmd = f'SELECT * FROM {self.__Table} WHERE url = "{url}"'
        cmd = DB.readData(cmd, True)
        if cmd:
            self.__init__(*cmd)
        

#x=Profile(1, 'a','a','a','a')
#x.getUsuario("jeff")
    