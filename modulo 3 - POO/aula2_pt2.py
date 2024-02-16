# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host="localhost") -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user)-> None:
        self.user = user
    def set_password(self, password) -> None:
        self.password = password

    @classmethod
    def connection_with_auth(cls,user: str ,password: str | int ):
        connection = cls()
        connection.user = user
        connection.password = password
        
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)


    def connection_log(msg):
        print('LOG:', msg)
        

c1 = Connection.connection_with_auth('jota', 'apenas123')
print(c1.user, c1.password)