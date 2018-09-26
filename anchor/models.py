from django.db import models
from google_api.drive_api.basic import DriveApi

def compressString(data):
    data.lower()
    spl=data.split(' ')
    compressed=""
    for word in spl:
        compressed+=word
    return compressed


class BasicProfile:

    def __init__(self,userid,password):
        self.userid=compressString(userid)
        self.password=password
        self.gdrive=DriveApi()

    def __str__(self):
        return self.userid

    #def get_absolute_url(self):
        #return "/profiles/%i" %self.userid

    def isValid(self):
        basicProfileList=self.gdrive.basicDownloadToString('basic_profiles.txt').split('\n')
        for line in basicProfileList:
            print(line)
            data=line.split(' ')
            if(self.userid==data[0] and self.password==data[1]):
                return True
        return False


    def create(self):
        info='\n'+self.userid+' '+self.password
        self.gdrive.appendStringToFile(info,'basic_profiles.txt')
        self.gdrive.createFile('basic_info_user_'+self.userid+'.txt')
        self.gdrive.createFile('chat_history_user_'+self.userid+'.txt')



    def delete(self):
        a=2
