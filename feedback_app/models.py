from django.db import models

# Create your models here.
class Analytics(models.Model):
    name = models.CharField(max_length=40)
    competen = models.IntegerField(default = 1)
    teach = models.IntegerField(default = 1)
    punc = models.IntegerField(default = 1)
    prac = models.IntegerField(default = 1)
    approach = models.IntegerField(default = 1)
    classcontrol = models.IntegerField(default = 1)