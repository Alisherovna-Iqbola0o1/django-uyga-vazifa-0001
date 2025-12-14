from django.db import models

# Create your models here.
class Komputer(models.Model):
    name = models.CharField(max_length=200)
    brend = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='komputer/')
    desc = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField()
    xotira = models.CharField(max_length=50)
    ram =  models.CharField(max_length=50)
    ekran_olchami = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name
