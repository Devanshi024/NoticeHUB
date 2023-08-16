from django import forms
from .models import *

class PostModelForm(forms.ModelForm):
    class Meta:
        model = postmodel
        fields = ('title','content','Professor','image')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = postmodel
        fields = ('title', 'content','Professor','image')

