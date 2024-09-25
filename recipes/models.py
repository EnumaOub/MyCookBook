from django.db import models

class recipe(models.Model):
    name = models.CharField(max_length=50)
    time = models.IntegerField(default=10)


