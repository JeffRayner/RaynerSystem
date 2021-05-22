from App import Conexao as DB

class Profile():
    __Table= "PROFILE"

    def __init__(self, ID=None, url="", name="", title="", email=""):
        self.__ID = ID
        self.__url = url
        self.name = name
        self.title = title
        self.email = email

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, id):
        self.__ID = id

    @property
    def url(self):
        return self.__url
    