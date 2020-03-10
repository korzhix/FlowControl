from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SfeduStuden(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sfedu_pass = models.CharField(widget=forms.PasswordInput)
    sfedu_username = models.CharField()