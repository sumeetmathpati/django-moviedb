from django.db import models

class Movie(models.Model):

    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name