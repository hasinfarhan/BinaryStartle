from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload



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
        return file_id
