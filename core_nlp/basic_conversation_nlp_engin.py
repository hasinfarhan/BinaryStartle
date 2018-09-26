from google_api.drive_api.basic import DriveApi

import os
import datetime


class TokProcess:

    def __init__(self,userid):
        self.userid=userid
        self.efficiency=1.00


    def pass0(self,value):
        music_words= [ 'gaan','song','music']
        if value.lower() in music_words:
            return True
        else:
            return False


    def generateReply(self,usertext):
        bottext=""
        rawtext=usertext.lower()
        wordlist=rawtext.split(' ')

        if self.pass0(rawtext):
            bottext="Eita shunte paren - https://www.youtube.com/watch?v=DWagZiMA3LE , cold gaan ekta"
        else:
            bottext="Bujhina bhai ki bolen!"



        self.updateHistory(usertext,bottext)
        return bottext

    def updateHistory(self,usertext,bottext):
        update=""
        update+='\n\n'+self.userid+'-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+usertext
        update+='\nTok-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+bottext

        gdrive=DriveApi()
        if self.userid=='':
            gdrive.appendStringToFile(update,'toklog.txt')
        else:
            gdrive.appendStringToFile(update,'chat_history_user_'+self.userid+'.txt')
