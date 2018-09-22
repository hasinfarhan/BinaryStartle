from django.http import HttpResponse,HttpResponseRedirect
from google_api.drive_api.demo import DriveApi
from django.shortcuts import render,redirect
from django.conf import settings



def index(request):
    gdrive=DriveApi()
    content=gdrive.demo1()
    return render(request,'anchor/landing.html',{'content_0':content})
