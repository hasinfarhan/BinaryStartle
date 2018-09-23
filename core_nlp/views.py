from django.http import HttpResponse,HttpResponseRedirect
from google_api.drive_api.demo import DriveApi
from django.shortcuts import render,redirect
from django.conf import settings

from .forms import BasicBotConversationForm

def index(request):
    gdrive=DriveApi()
    oldBasicBotConversationForm=BasicBotConversationForm(request.POST)
    newBasicBotConversationForm=BasicBotConversationForm()

    if oldBasicBotConversationForm.is_valid():
        newBasicBotConversationForm.fields['bottext'].initial=oldBasicBotConversationForm.cleaned_data.get('usertext')
    else:
        print("oldBasicBotConversationForm.errors")
        print(oldBasicBotConversationForm.errors)

    return render(request,'core_nlp/core_nlp.html',{'basic_bot_conversation_form':newBasicBotConversationForm})
