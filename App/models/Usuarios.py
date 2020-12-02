from App import Conexao as DB

class Usuario():
    __Table= "USUARIOS"

    def __init__(self, ID=None, Usuario="", Senha="", Email="", ID_Nivel=None):
        self.ID = ID
        self.Usuario = Usuario
        self.Senha = Senha
        self.Email = Email
        self.ID_Nivel = ID_Nivel
        
    def __str__(self):
        return f'ID={self.ID}\nUsuario={self.Usuario}\nSenha={self.Senha}\nEmail={self.Email}\nID_Nivel={self.ID_Nivel}'
    
    def getValues(self):
        return {"id":self.ID, "usuario":self.Usuario, "senha":self.Senha, \
            "email":self.Email, "nivel":self.ID_Nivel}

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, id):
        self.__ID = id

    @property
    def Usuario(self):
        return self.__Usuario
    @Usuario.setter
    def Usuario(self, usuario):
        self.__Usuario =  usuario.lower()

    @property
    def Senha(self):
        return ""
    @Senha.setter
    def Senha(self, senha):
        self.__Senha = senha
    
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, email):
        self.__Email = email.lower()

    @property
    def ID_Nivel(self):
        return self.__ID_Nivel
    @ID_Nivel.setter
    def ID_Nivel(self, id):
        self.__ID_Nivel = id

    # retorna Dicionario da Classe
    def getValues(self):
        return {"id":self.ID, "usuario":self.Usuario, "senha":self.Senha, \
            "email":self.Email, "nivel":self.ID_Nivel}

    # Func para validar valores de String
    def __validar(self, value):
        if isinstance(value, str) and len(value) >= 3:
            return True
        print ("Erro Validar:", value)
    
    # Func para validar valores Inteiros
    def __validarID(self, value):
        if isinstance(value, int) and value > 0:
            return True
        print ("Erro Validar:", value)

    # Cadastrar Usuario
    def criarUsuario(self):
        if self.__validar(self.Usuario) and self.__validar(self.Senha) \
            and self.__validar(self.Email) and self.__validarIDNivel(self.ID_Nivel):
            sql = f'INSERT INTO {self.__Table} (Usuario, Senha, Email, ID_Nivel) VALUES ("{self.__Usuario}","{self.__Senha}","{self.__Email}",{self.__ID_Nivel})'
            return DB.queryDB(sql)

    def validarLogin(self):
        #print (self.Usuario,self.Senha )
        sql = f'SELECT * FROM {self.__Table} WHERE Usuario = "{self.Usuario}" AND Senha = "{self.__Senha}" '
        sql = DB.readData(sql, True)
        if sql:
            self.__init__(*sql)
            return True

    def listarUsuario(self):
        lista = []
        sql = f'SELECT * FROM {self.__Table}'
        sql = DB.readData(sql)
        if sql:
            for i in sql:
                i = Usuario(*i)
                lista.append(i.getValues())
            return lista
    
    def alterarUsuario(self, novoUsuario):
        if self.__validar(novoUsuario):
            novoUsuario = novoUsuario.lower()
            sql = f'UPDATE {self.__Table} SET Usuario = "{novoUsuario}" WHERE ID = {self.ID}'
            sql = DB.queryDB(sql)
            if sql:
                self.Usuario = novoUsuario
            return sql
    
    def alterarSenha(self, novaSenha):
        if self.__validar(novaSenha):
            sql = f'UPDATE {self.__Table} SET Senha = "{novaSenha}" WHERE ID = {self.ID}'
            sql = DB.queryDB(sql)
            if sql:
                self.Senha = novaSenha
            return sql  
    
    def alterarEmail(self, novoEmail):
        if self.__validar(novoEmail):
            novoEmail = novoEmail.lower()
            sql = f'UPDATE {self.__Table} SET Email = "{novoEmail}" WHERE ID = {self.ID}'
            sql = DB.queryDB(sql)
            if sql:
                self.Email = novoEmail
            return sql 
    
    def alterarIdNivel(self, novoIdNivel):
        if self.__validarID(novoIdNivel):
            sql = f'UPDATE {self.__Table} SET ID_Nivel = "{novoIdNivel}" WHERE ID = {self.ID}'
            if sql:
                self.ID_Nivel = novoIdNivel
            return sql 
    
    def excluirUsuario(self):
        pass


