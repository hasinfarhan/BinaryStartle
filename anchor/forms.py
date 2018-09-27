from django import forms
from django.core.exceptions import ValidationError

from .models import BasicProfile



def ForbiddenUsernameValidator(value):
    forbidden_words = ['###','admin', 'settings', 'news', 'about', 'help',
                           'signin', 'signup', 'signout', 'terms', 'privacy',
                           'cookie', 'new', 'login', 'logout', 'administrator',
                           'join', 'account', 'username', 'root', 'blog',
                           'user', 'users', 'billing', 'subscribe', 'reviews',
                           'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                           'home', 'job', 'jobs', 'contribute', 'newsletter',
                           'shop', 'profile', 'register', 'auth',
                           'authentication', 'campaign', 'config', 'delete',
                           'remove', 'forum', 'forums', 'download',
                           'downloads', 'contact', 'blogs', 'feed', 'feeds',
                           'faq', 'intranet', 'log', 'registration', 'search',
                           'explore', 'rss', 'support', 'status', 'static',
                           'media', 'setting', 'css', 'js', 'follow',
                           'activity', 'questions', 'articles', 'network', ]

    if value.lower() in forbidden_words:
        raise ValidationError('This is a reserved id')





class BasicLoginForm(forms.Form):

    userid=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'User Id','autofocus':'autofocus'}),
        max_length=20,
        required=True,
        )

    password=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password'}),
        max_length=25,
        required=True,
        )
    def __init__(self, *args, **kwargs):
        super(BasicLoginForm, self).__init__(*args, **kwargs)
        self.after_login_url=''

    def clean(self):
        super(BasicLoginForm, self).clean()
        uid=self.cleaned_data.get('userid')
        pswd=self.cleaned_data.get('password')

        if not uid:
            raise forms.ValidationError("User id required!")

        if not pswd:
            raise forms.ValidationError("Password required!")


        if(' ' in pswd or '\n' in pswd):
            raise forms.ValidationError("Password can't contain newline or space!")

        profile=BasicProfile(uid,pswd)

        if not profile.isValid():
            raise forms.ValidationError("Profile doesn't exist or wrong password!")

        return self.cleaned_data

    def set_after_login_url(self,url):
        self.after_login_url=url



class BasicSignupForm(forms.Form):

    userid=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'User Id','autofocus':'autofocus'}),
        max_length=20,
        required=False,
        )

    password=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password'}),
        max_length=25,
        required=False,
        )

    conf_password=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Confirm Password'}),
        max_length=25,
        required=True,
        )


    def __init__(self, *args, **kwargs):
        super(BasicSignupForm, self).__init__(*args, **kwargs)
        self.after_signup_url=''

    def clean(self):
        super(BasicSignupForm, self).clean()
        uid=self.cleaned_data.get('userid')
        pswd=self.cleaned_data.get('password')
        cpswd=self.cleaned_data.get('conf_password')

        ForbiddenUsernameValidator(uid)

        if not uid:
            raise forms.ValidationError("User id required!")

        if not pswd:
            raise forms.ValidationError("Password required!")

        if not cpswd:
            raise forms.ValidationError("Confirm password!")

        if pswd!=cpswd:
            raise forms.ValidationError("Sorry, the passwords didn't match!")
        if(' ' in pswd or '\n' in pswd):
            raise forms.ValidationError("Password can't contain newline or space!")

        profile=BasicProfile(uid,pswd)

        if profile.isValid():
            raise forms.ValidationError("Profile exists!")

        profile.create()

        return self.cleaned_data

    def set_after_signup_url(self,url):
        self.after_signup_url=url
