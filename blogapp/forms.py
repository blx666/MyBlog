# from forms import *
from django import forms
from blogapp.models import *


class userForm(forms.ModelForm):
    class Meta:
        model = UserBlog
        fields = ['name', 'pwd', 'phone']


class CalendarWiget(forms.Textarea):
    class Media:
        css = {
            'all': ('temp.css',),
        }
        # js = ('temp.js',)


class LoinForm(forms.Form):
    CHOICES = (('1', 'First',), ('2', 'Second',), ('3', 'Third',))
    name = forms.CharField(label=u'title', widget=forms.TextInput(attrs={'size': '40'}))
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.ChoiceField(widget=CalendarWiget)


    pas = forms.ChoiceField(choices=CHOICES)


