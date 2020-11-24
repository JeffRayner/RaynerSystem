import sqlite3
#import logging as log
#log.basicConfig(filename='Conexaolog.txt')

__DB = 'DataBase.db'

def __ErrorLog(error):
    print (error)
    # Adicionar o comando para registar Log de Erro

#funcao para realizar atualização no banco
def queryDB(cmd):
    try:
        with sqlite3.connect(__DB) as conn:
            cursor = conn.cursor()
            cursor.execute(cmd)
            conn.commit()
            return True
    except Exception as error:
        __ErrorLog(error)

#funcao para Multiplos cadastros no banco
def manyQueryDB(cmd, listaValores):
    try:
        with sqlite3.connect(__DB) as conn:
            cursor = conn.cursor()
            cursor.executemany(cmd, listaValores)
            conn.commit()
            return True
    except Exception as error:
        __ErrorLog(error)

#funcao para realizar consulta no banco 
def readData(cmd, one=False):
    res = None
    try:
        with sqlite3.connect(__DB) as conn:
            cursor = conn.cursor()
            cursor.execute(cmd)
            res = cursor.fetchall()
            if one and res:
                return res[0]
        return res
    except Exception as error:
        __ErrorLog(error)
    

