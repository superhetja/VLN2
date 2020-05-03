from django.forms import ModelForm, widgets
from django import forms
from user.models import User

class UserUpdateForm(ModelForm):
    #image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control' }))
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.PasswordInput(attrs={ 'class': 'form-control'}),
            'profile_pic': widgets.TextInput(attrs={'class': 'form-control'}),
            'has_address': widgets.CheckboxInput(attrs={'class': 'form-control'})
            #Todo: Fix this page
        }

class UserCreateForm(ModelForm):
    #image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control' }))
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.PasswordInput(attrs={ 'class': 'form-control'}),
            'profile_pic': widgets.TextInput(attrs={'class': 'form-control'}),
            'has_address': widgets.CheckboxInput(attrs={'class': 'form-control'})
            #Todo: Fix this page
        }