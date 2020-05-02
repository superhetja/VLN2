from django.db import models
# Tools -> Run manage.py Task.. -> makemigrations


class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=999, blank=True)
    has_address = models.BooleanField(default=False)


class UserBilling(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_nr = models.IntegerField()
    postal_code = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


