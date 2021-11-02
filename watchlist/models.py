from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

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
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True, related_name='media')


    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    media = models.ForeignKey(Media, blank=True, null=True, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateField(auto_now_add=True)

    def _str__(self):
        return str(self.rating) + ": " + media.title
    
