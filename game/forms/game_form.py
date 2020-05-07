from django.forms import ModelForm, widgets
from django import forms
from game.models import Game


class GameCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Game
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'type_id': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={'class': 'form-control'})
        }