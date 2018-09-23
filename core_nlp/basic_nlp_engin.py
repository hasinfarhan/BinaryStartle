from google_api.drive_api.basic import DriveApi

import os
import datetime


class TokProcess:

    def __init__(self):
        self.efficiency=1.00

    def generateReply(self,usertext):
        bottext=usertext

        self.updateHistory(usertext,bottext)
        return bottext

    def updateHistory(self,usertext,bottext):
        gdrive=DriveApi()
        history=gdrive.basicDownload('toklog.txt')
        updatedhistory=history
        updatedhistory+='\n\nUser-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+usertext
        updatedhistory+='\nTok-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+bottext
        file=open('google_api/drive_api/toklog.txt','w')
        file.write(updatedhistory)
        file.close()
        gdrive.deleteFile('toklog.txt')
        gdrive.basicUpload('toklog.txt','google_api/drive_api/toklog.txt','text/plain')
        os.remove('google_api/drive_api/toklog.txt')
