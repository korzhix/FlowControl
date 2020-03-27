from django.db import models
from django import forms
from django.contrib.auth.models import User




# Create your models here.
class SfeduStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sfedu_pass = models.CharField()
    sfedu_username = models.CharField()
    schadule = models.CharField()
    score_line = models.CharField()
    sfedu_username = models.CharField()
