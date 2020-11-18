import sqlite3
#import logging as log
#log.basicConfig(filename='Conexaolog.txt')

__DB = 'DataBase.db'

#funcao para realizar atualização no banco
def queryDB(cmd):
    with sqlite3.connect(__DB) as conn:
        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()
        return True

#funcao para realizar consulta no banco 
def readData(cmd, one=False):
    res = None
    with sqlite3.connect(__DB) as conn:
        cursor = conn.cursor()
        cursor.execute(cmd)
        res = cursor.fetchall()
        if one and res:
            return res[0]
    return res

