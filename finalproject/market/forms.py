from profile import Profile

from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'




class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = []
        widgets = {
            "password": forms.PasswordInput()
        }

class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'
        exclude = []
        widgets = {
            "password": forms.PasswordInput()
        }

