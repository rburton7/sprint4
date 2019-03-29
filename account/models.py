from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog import models as cmod

# Create your models here.

class User(AbstractUser):
    birthdate = models.DateTimeField()
    favcolor = models.TextField()

    def get_shopping_cart(self):
            sale = cmod.Sale.objects.filter(user=self, purchased=None).first()
            if sale is None:
                sale = cmod.Sale()
                sale.user = self
                sale.save()
            return sale