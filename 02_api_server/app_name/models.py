from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=5)
    age = models.IntegerField()