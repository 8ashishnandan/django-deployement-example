from django import forms
from WebApp.models import User
'''
class NewUser(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    '''

class NewUser(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'
