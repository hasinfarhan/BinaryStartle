from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

import io
import os


def fileMimeExtractor(filename):
    mimedict={'txt':'text/plain','jpg':'image/jpeg'}
    rev=filename[::-1]
    revext=""
    for c in rev:
        if c=='.':
            break
        revext+=c

    ext=revext[::-1]
    return mimedict[ext]



class DriveApi:

    def __init__(self):
        self.scopes = 'https://www.googleapis.com/auth/drive'
        self.credential='google_api/drive_api/credentials/client_secret.json'
        store = file.Storage('google_api/drive_api/credentials/client_token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self.credential,self.scopes)
            creds = tools.run_flow(flow, store)
        self.service = build('drive','v3',http=creds.authorize(Http()))

    def ifExist(self,filename):
        query="name='"+filename+"'"
        results = self.service.files().list(q=query).execute()
        items = results.get('files', [])
        if items:
            return True
        else:
            return False

    def hala(self,filename):
        return fileMimeExtractor(filename)

    def basicDownloadToBinary(self,filename):
        if not self.ifExist(filename):
            self.createFile(filename)

        query="name='"+filename+"'"
        results = self.service.files().list(q=query).execute()
        items = results.get('files', [])
        file_id = items[0].get('id')

        request = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO('google_api/drive_api/demoTEMP.txt',mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False

        while done is False:
            status, done=downloader.next_chunk()

        tempfile=open('google_api/drive_api/demoTEMP.txt',mode='rb')
        data=b''
        for line in tempfile:
            data+=line

        tempfile.close()
        os.remove('google_api/drive_api/demoTEMP.txt')
        return data

    def basicDownloadToString(self,filename):
        return self.basicDownloadToBinary(filename).decode("utf-8")


    def basicUpload(self,filename,filepath):
        file_metadata = {'name': filename}
        media = MediaFileUpload(filepath,
                                mimetype=fileMimeExtractor(filename))
        file = self.service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()


    def createFile(self,filename):
        if not self.ifExist(filename):
            tempfile=open('google_api/drive_api/createTEMP.txt',mode='wb')
            data="### ### ###"
            tempfile.write(data.encode('utf-8'))
            tempfile.close()
            self.basicUpload(filename,'google_api/drive_api/createTEMP.txt')
            os.remove('google_api/drive_api/createTEMP.txt')
            return True
        else:
            return False


    def deleteFile(self,filename):
        if self.ifExist(filename):
            query="name='"+filename+"'"
            results = self.service.files().list(q=query).execute()
            items = results.get('files', [])
            file_id = items[0].get('id')
            self.service.files().delete(fileId=file_id).execute()
            return True
        else:
            return False


    def getFileMimeType(self,filename):
        if self.ifExist(filename):
            query="name='"+filename+"'"
            results = self.service.files().list(q=query).execute()
            items = results.get('files', [])
            file_mime = items[0].get('mimeType')
            return file_mime
        else:
            return None

    def appendBinaryToFile(self,data,filename):
        if not self.ifExist(filename):
            self.createFile(filename,fileMimeExtractor(filename))

        history=self.basicDownloadToBinary(filename)
        file=open('google_api/drive_api/appendTEMP.txt','wb')
        file.write(history)
        file.close()
        file=open('google_api/drive_api/appendTEMP.txt','ab')
        file.write(data)
        file.close()
        mimeType=self.getFileMimeType(filename)
        self.deleteFile(filename)
        self.basicUpload(filename,'google_api/drive_api/appendTEMP.txt')
        os.remove('google_api/drive_api/appendTEMP.txt')

    def appendStringToFile(self,data,filename):
        self.appendBinaryToFile(data.encode('utf-8'),filename)
