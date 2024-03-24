from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=155, null=True, blank=True)
    description = models.TextField(blank=True, null=True, max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
