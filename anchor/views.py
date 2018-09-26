from django.http import HttpResponse,HttpResponseRedirect
from google_api.drive_api.basic import DriveApi
from django.shortcuts import render,redirect
from django.conf import settings



def index(request):
    gdrive=DriveApi()
    content=gdrive.basicDownloadToString('hello.txt').split('\n')
    return render(request,'anchor/landing.html',{'content_0':content})

def forbidden_message(request):
    return render(request,'anchor/includes/forbidden_msg.html')
