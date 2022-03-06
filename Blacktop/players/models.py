from django.db import models

# Create your models here.
class Player(models.Model):
    team=models.CharField(max_length=20)
    name=models.CharField(max_length=80)
    pos=models.CharField(max_length=80)
    ovr=models.IntegerField(default=60)


