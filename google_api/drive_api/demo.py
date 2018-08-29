from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

import io


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

    def demo1(self):
        results = self.service.files().list(q="name='hello.txt'").execute()
        items = results.get('files', [])
        file_id = items[0].get('id')

        request = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO('google_api/drive_api/demoTEMP.txt',mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done=downloader.next_chunk()
            
        tempfile=open('google_api/drive_api/demoTEMP.txt',mode='rb')
        data=tempfile.read()
        tempfile.close()
        return data
