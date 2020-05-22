import os
import json
import users
from Globals import globlas
from getpass import getpass
from DB import db
import logging
import hashlib


logging.basicConfig(
    level=logging.DEBUG
)


def file_exists(file_name):
    """check if file exists"""
    if os.path.isfile(file_name):
        return True
    return False

def get_data_json(file_name):
    """Return object with data from init.json in format Json"""
    with open(file_name) as f:
        data = json.load(f)    
    return data

def set_data_db(data):
    """set values from init.json to Globals"""
    globlas.DB = data["db"]
    globlas.USER_DB = data["user"]
    globlas.PASSWD_DB = data["passwd"]
    globlas.SERVER = data["server"]
    return True

def get_connection_db(data):
    """This funtion return object connection to DB"""
    try:
        if set_data_db(data):
            con = db.connection_db(db=globlas.DB,
                                   user_db=globlas.USER_DB,
                                   passwd_db=globlas.PASSWD_DB,
                                   server=globlas.SERVER)
            return con
    except Exception as e:
        logging.debug("utils.get_connection_db",e)



class UserMethods:
    
    @staticmethod
    def create_user():
        """set data from user to create instance User"""
        name = input("Name> ")
        last_name = input("Last Name> ")
        passwd = getpass("Password> ")
        hash_object = hashlib.md5(passwd.encode())
        passwd_md5 = hash_object.hexdigest()
        new_user = users.User(name, last_name, passwd_md5)
        return new_user
    
    @staticmethod
    def insert_user(con, new_user):
        """:params: Object connection to DB and intance User
            Insert User on Database
        """
        try:
            cur = con.cursor()
            sql = "INSERT INTO users (name, last_name, password) VALUES('{}', '{}', '{}')".format(
                    new_user.name,
                    new_user.last_name,
                    new_user.passwd)
            cur.execute(sql)
            con.commit()
        except Exception as e:
            logging.debug("utils.insert_user", e)
        

if __name__ == "__main__":
    if file_exists(globlas.INIT_FILE):
        data = get_data_json(globlas.INIT_FILE)
        con = get_connection_db(data)
        if db.login(con):
            new_user = UserMethods.create_user()
            UserMethods.insert_user(con, new_user)
            db.close_db(con)
        else:
            print("Usuario o Contraseña incorrecto")
            db.close_db(con)
    else:
        print("no existe")
    
    
    