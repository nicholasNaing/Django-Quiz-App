from django import forms
from django.contrib.auth.models import User
from .models import profile

class update_user(forms.ModelForm):
    email = forms.EmailField()
    class Meta :
        model=User
        fields = ['username','email']

class update_profile(forms.ModelForm):
    class Meta :
        model=profile
        fields = ['image']