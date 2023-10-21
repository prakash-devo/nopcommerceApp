import configparser

config=configparser.RawConfigParser()
config.read(".\\Configeration\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username
    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password