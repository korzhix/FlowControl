from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class SfeduStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sfedu_pass = models.CharField()
    sfedu_username = models.CharField()
    schadule = models.CharField()
    score_line = models.CharField()
    sfedu_username = models.CharField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sfedu_pass = models.CharField(max_length=50)
    sfedu_username = models.CharField(max_length=50)
    sfedu_schadule = models.CharField(max_length=5000, default='empty')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
