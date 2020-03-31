from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Settings
from .models import Sidebar

class SettingsForm(ModelForm):

    class Meta:
        model = Settings
        fields = ('url_of_notes', 'url_of_disk')
        labels = {'url_of_notes': 'Сервис заметок', 'url_of_disk': 'Сервис хранилища данных'}

class SidebarForm(forms.Form):
    choices = [(item.name, item.name) for item in Sidebar.objects.all()]
    name = forms.ChoiceField(choices=choices)
    homework_link = forms.URLField()
    aims_link = forms.URLField()
    todo_link = forms.URLField()

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('sfedu_username', 'sfedu_pass')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
