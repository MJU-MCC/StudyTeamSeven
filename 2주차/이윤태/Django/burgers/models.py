from django.db import models

class Burger(models.Model):
    name = models.CharField(max_length = 20) #문자열
    price = models.IntegerField(default = 0) #정수
    calrories = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
# Create your models here.
