from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=20)