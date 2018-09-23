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
        update=""
        update+='\n\nUser-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+usertext
        update+='\nTok-'+datetime.datetime.now().strftime('%m/%d/%Y')+": "+bottext

        gdrive=DriveApi()
        gdrive.appendStringToFile(update,'toklog.txt')
