from django.contrib.auth.models import User
from django.db import models
# Tools -> Run manage.py Task.. -> makemigrations


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    profile_image = models.CharField(max_length=999, blank=True)

