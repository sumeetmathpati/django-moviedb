from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=63)
    about = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self): 
        return self.name

class Media(models.Model):

    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    released_date = models.DateField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name="media", null=True, blank=True)


    def __str__(self):
        return self.name