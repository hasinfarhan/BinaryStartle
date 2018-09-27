from django import forms
from django.core.exceptions import ValidationError



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


    def clean(self):
        super(BasicBotConversationForm, self).clean()

        utx=self.cleaned_data.get('usertext')
        btx=self.cleaned_data.get('bottext')

        if not utx:
            raise forms.ValidationError("Say something first!")


        return self.cleaned_data
