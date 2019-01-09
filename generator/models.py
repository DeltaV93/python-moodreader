from django.db import models

class Dictionary(models.Model):
    word = models.CharField(max_length=200)
    word_value = models.IntegerField()
