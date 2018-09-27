from google_api.drive_api.basic import DriveApi

import os
import datetime


class TokProcess:

    def __init__(self,userid,usertext):
        self.userid=userid
        self.efficiency=1.00
        self.usertext=usertext
        self.rawtext=usertext.lower()
        self.wordlist=self.rawtext.split(' ')


    def pass0(self):
        music_words= ['gaan','song','music','romantic','cold','dance','slow']
        cnt=0;
        for w in self.wordlist:
            if w in music_words:
                cnt+=1
        return cnt

    def pass1(self):
        music_words= ['gaan','song','music','romantic','beat','dance']
        cnt=0;
        for w in self.wordlist:
            if w in music_words:
                cnt+=1
        return cnt

    def pass1(self):
        music_words= ['gaan','song','music',]
        cnt=0;
        for w in self.wordlist:
            if w in music_words:
                cnt+=1
        return cnt

    def generateReply(self):
        bottext=""
        if self.pass0()>3:
            bottext="You can listen to - https://www.youtube.com/watch?v=DWagZiMA3LE "
        elif self.pass1()>3:
            bottext="You can listen to -  https://www.youtube.com/watch?v=FQS7i2z1CoA "
        else:
            bottext="I don't know what to say!"


        self.updateHistory(bottext)
        return bottext

    def updateHistory(self,bottext):
        update=""
        update+='\n\n'+self.userid+'-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+self.usertext
        update+='\nTok-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+bottext

        gdrive=DriveApi()
        if self.userid=='':
            gdrive.appendStringToFile(update,'toklog.txt')
        else:
            gdrive.appendStringToFile(update,'chat_history_user_'+self.userid+'.txt')
