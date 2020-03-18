from django import forms
from django.forms import ModelForm

from . models import *
from . forms import *

class PlayerForm(forms.ModelForm):

    class Meta:
       model = Player
       fields = '__all__'