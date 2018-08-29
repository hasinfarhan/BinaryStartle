from django.http import HttpResponse
from google_api.drive_api.demo import DriveApi

def index(request):
    gdrive=DriveApi()
    fid=gdrive.demo1()
    #fid="ddsdsdsd"
    return HttpResponse(fid)
