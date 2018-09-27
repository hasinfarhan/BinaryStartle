from django.http import HttpResponse,HttpResponseRedirect
from google_api.drive_api.basic import DriveApi
from django.shortcuts import render,redirect
from django.conf import settings

from .forms import BasicBotConversationForm
from anchor.forms import BasicLoginForm
from anchor.forms import BasicSignupForm
from .basic_conversation_nlp_engin import TokProcess


from anchor.models import BasicProfile




def index(request):
    if not request.POST:
        return render(request,'core_nlp/talk2pok.html',{'basic_bot_conversation_form':BasicBotConversationForm()})

    oldBasicBotConversationForm=BasicBotConversationForm(request.POST)
    newBasicBotConversationForm=BasicBotConversationForm()

    usertext=""
    bottext=""

    if oldBasicBotConversationForm.is_valid():
        usertext=oldBasicBotConversationForm.cleaned_data.get('usertext')
    else:
        return render(request,'core_nlp/talk2pok.html',{'basic_bot_conversation_form':oldBasicBotConversationForm})

    userid=''
    if 'basicid' in request.session:
        userid=request.session['basicid']
    bot=TokProcess(userid,usertext)
    bottext=bot.generateReply()
    newBasicBotConversationForm.fields['bottext'].initial=bottext
    return render(request,'core_nlp/talk2pok.html',{'basic_bot_conversation_form':newBasicBotConversationForm})





def login_signup_page(request):
    loginform=BasicLoginForm()
    signupform=BasicSignupForm()
    loginform.set_after_login_url('/core_nlp/login')
    signupform.set_after_signup_url('/core_nlp/signup')
    return render(request,'core_nlp/talk2pok_login_signup.html',{'loginform':loginform,'signupform':signupform})


def login(request):
    loginform=BasicLoginForm(request.POST)
    if loginform.is_valid():
        request.session['basicid']=loginform.cleaned_data.get('userid')
        return redirect('/core_nlp')
    else:
        signupform=BasicSignupForm()
        signupform.set_after_signup_url('/core_nlp/signup')
        return render(request,'core_nlp/talk2pok_login_signup.html',{'loginform':loginform,'signupform':signupform})

def logout(request):
    del request.session['basicid']
    return redirect('/core_nlp')



def signup(request):
    signupform=BasicSignupForm(request.POST)
    if signupform.is_valid():
        request.session['basicid']=signupform.cleaned_data.get('userid')
        return redirect('/core_nlp')
    else:
        loginform=BasicLoginForm()
        loginform.set_after_login_url('/core_nlp/loginup')
        return render(request,'core_nlp/talk2pok_login_signup.html',{'loginform':loginform,'signupform':signupform})

def chathistory(request):
    gdrive=DriveApi()
    chathistory=gdrive.basicDownloadToString('chat_history_user_'+request.session['basicid']+'.txt').split('\n')
    return render(request,'core_nlp/talk2pok_chat_history.html',{'chathistory':chathistory})

def pokfaq(request):
    return render(request,'core_nlp/talk2pok_faq.html')



def pokprofile(request):
    return render(request,'core_nlp/talk2pok_profile.html')



#def analytics(request):
    #return render(request,'core_nlp/tok2pok_login.html',{'basic_bot_conversation_form':newBasicBotConversationForm})
