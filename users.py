class User:
    def __init__(self, name, last_name, passwd):
        self.__name = name
        self.__last_name = last_name
        self.__passwd = passwd
    
    def __str__(self):
        return "{}".format(self.__name)
    
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, value):
        self.__last_name = value
    
    def get_passwd(self):
        return self.__passwd
    
    def set_passwd(self, value):
        self.__passwd = value
        
        
    name = property(get_name, set_name)
    last_name = property(get_last_name, set_last_name)
    passwd = property(get_passwd, set_passwd)
    

if __name__ == "__main__":
    fide = User(2, "fide", "Ramirez", "forever11")
    print(fide)
    
        