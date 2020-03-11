from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class SfeduStuden(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # sfedu_pass =
    # sfedu_username =