from django.db import models
from django.utils import timezone


class Dictionary(models.Model):
    word = models.CharField(max_length=200)
    word_value = models.IntegerField()

    def __str__(self):
        return self.word


class Entry(models.Model):
    entry_title = models.CharField(max_length=140)
    entry = models.CharField(max_length=1400)
    gradient_color_stop_1 = models.CharField(max_length=7, blank=True)
    gradient_color_stop_2 = models.CharField(max_length=7, blank=True)
    gradient_color_stop_3 = models.CharField(max_length=7, blank=True)
    pub_date = models.DateTimeField('date entered', blank=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.entry_title

# Add complexity by adding a second model with a foreign key.
