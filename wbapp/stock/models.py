from django.db import models

# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=255)
    count = models.TextField(blank=True)
    t1 = models.DateTimeField(auto_now_add=True)
    t2 = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")