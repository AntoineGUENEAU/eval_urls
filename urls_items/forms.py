from django import forms
from users.forms import ModelFormWithSubmit
from .models import Url

class UrlForm(ModelFormWithSubmit):
    
    class Meta:
        model = Url
        fields = ('name',)