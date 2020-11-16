import sqlite3
#import logging as log
#log.basicConfig(filename='Conexaolog.txt')

__DB = 'DataBase.db'

def __connectDB():
    try:
        return sqlite3.connect(__DB)
    except:
        print ('erro login')

def __getCursor(conn):
    try:
        return conn.cursor()
    except:
        print('ok')

def __closeDB(conn):
    conn.close()
#funcao para realizar atualização no banco
def queryDB(cmd):
    con = __connectDB()
    cursor = __getCursor(con)
    cursor.execute(cmd)
    con.commit()
    __closeDB(con)
    return True

#funcao para realizar consulta no banco 
def readData(cmd, one=False):
    con = __connectDB()
    cursor = __getCursor(con)
    cursor.execute(cmd)
    res = cursor.fetchall()
    __closeDB(con)
    if one and res:
        return res[0]
    return res

