from django.db import models

# Create your models here.


class leaderboard(models.Model):
    Username=models.CharField(max_length=225)
    Email=models.EmailField()
    Points_Scored=models.IntegerField()

