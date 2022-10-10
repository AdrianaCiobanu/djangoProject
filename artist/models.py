from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=40)
    song = models.CharField(max_length=50)
    album = models.CharField(max_length=30)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
