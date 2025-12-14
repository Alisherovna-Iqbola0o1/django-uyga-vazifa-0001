from django.db import models
from django.contrib.auth.models import User
from telefon.models import Telefon
# Create your models here.

class Savatcha(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telefon = models.ForeignKey(Telefon, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user.username} - {self.telefon.name}"


class Buyurtma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addres = models.CharField(max_length=50)
    telefon_raqam = models.CharField(max_length=20)
    jami_narx = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.user.username} - {self.jami_narx} UZS "