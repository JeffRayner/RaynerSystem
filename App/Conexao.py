import sqlite3
#import logging as log
#log.basicConfig(filename='DataBase-LOG.txt', enconding="utf-8")

__DB = 'NewDataBase.db'

def __ErrorLog(error):
    #log.error(error)
    print ("LOG:",error)

#funcao para realizar atualização no banco
def queryDB(cmd):
    try:
        with sqlite3.connect(__DB) as conn:
            cursor = conn.cursor()
            cursor.execute(cmd)
            conn.commit()
            return True
    except sqlite3.Error as error:
        __ErrorLog(error)

#funcao para Multiplos cadastros no banco
def manyQueryDB(cmd, listaValores):
    try:
        with sqlite3.connect(__DB) as conn:
            cursor = conn.cursor()
            cursor.executemany(cmd, listaValores)
            conn.commit()
        return True
    except sqlite3.Error as error:
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
                res = res[0]
    except sqlite3.Error as error:
        __ErrorLog(error)
    return res
    
#########################
#   Funcao para criar o banco de dados
#########################
