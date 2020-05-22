import psycopg2
from getpass import getpass
import hashlib

def connection_db(db, user_db, passwd_db, server):
    try:
        con = psycopg2.connect(host=server,
                               user=user_db,
                               password=passwd_db,
                               database=db)
        if con:
            print("Conexión hecha")
            return con
    except Exception as e:
        print(e)


def login(con):
    cur = con.cursor()
    user = input("Usuario> ")
    passwd = getpass("Contraseña> ")
    hash_object = hashlib.md5(passwd.encode())
    passwd_md5 = hash_object.hexdigest()
    sql = "SELECT * FROM users WHERE name='{}' AND password='{}'".format(user, passwd_md5)
    cur.execute(sql)
    us = cur.fetchone()
    if us is not None:
        print("Bienvenido {}".format(us[2]))
        return True
    return False
    
def close_db(con):
    con.close()


if __name__ == "__main__":
    connection_db()
    #show_users()
    login()