from django.http import HttpResponse,HttpResponseRedirect
from google_api.drive_api.basic import DriveApi
from django.shortcuts import render,redirect
from django.conf import settings

from .forms import BasicBotConversationForm
from .basic_nlp_engin import TokProcess

def index(request):
    oldBasicBotConversationForm=BasicBotConversationForm(request.POST)
    newBasicBotConversationForm=BasicBotConversationForm()
    bot=TokProcess()
    usertext=""
    bottext=""

    if oldBasicBotConversationForm.is_valid():
        usertext=oldBasicBotConversationForm.cleaned_data.get('usertext')
    else:
        print("oldBasicBotConversationForm.errors")
        print(oldBasicBotConversationForm.errors)

    if usertext!="":
        bottext=bot.generateReply(usertext)

    newBasicBotConversationForm.fields['bottext'].initial=bottext

    return render(request,'core_nlp/core_nlp.html',{'basic_bot_conversation_form':newBasicBotConversationForm})
