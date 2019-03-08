from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    birthdate = models.DateTimeField()
    favcolor = models.TextField()
