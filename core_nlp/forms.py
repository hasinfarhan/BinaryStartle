from django import forms
from django.core.exceptions import ValidationError



def ForbiddenWOrdValidator(value):
    forbidden_words = ['admin', 'settings', 'news', 'about', 'help',
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
        raise ValidationError('This is a reserved word.')





class BasicBotConversationForm(forms.Form):

    usertext=forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Speak Up!','rows':'5','autofocus':'autofocus'}),
        max_length=200,
        required=False,
        )

    bottext=forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control','rows':'5','readonly':'readonly'}),
        max_length=200,
        required=False,
        )
    def __init__(self, *args, **kwargs):
        super(BasicBotConversationForm, self).__init__(*args, **kwargs)
        #self.fields['usertext'].validators.append(ForbiddenWOrdValidator)

    def clean(self):
        super(BasicBotConversationForm, self).clean()
        return self.cleaned_data
