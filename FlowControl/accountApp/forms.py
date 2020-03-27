from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile



class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('sfedu_username', 'sfedu_pass')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
