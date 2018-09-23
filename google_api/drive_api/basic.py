from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

import io
import os


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

    def basicDownload(self,filename):
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
        data=""

        for line in tempfile:
            data+=line.decode("utf-8")

        tempfile.close()
        os.remove('google_api/drive_api/demoTEMP.txt')
        return data


    def basicUpload(self,filename,filepath,mime):
        file_metadata = {'name': filename}
        media = MediaFileUpload(filepath,
                                mimetype=mime)
        file = self.service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID:'+file.get('id'))
        print('DoneUploading')


    def deleteFile(self,filename):
        query="name='"+filename+"'"
        results = self.service.files().list(q=query).execute()
        items = results.get('files', [])
        file_id = items[0].get('id')
        self.service.files().delete(fileId=file_id).execute()
