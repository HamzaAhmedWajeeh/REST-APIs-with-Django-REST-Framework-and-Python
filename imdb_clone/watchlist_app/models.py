from django.db import models

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    about = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=155, null=True, blank=True)
    storyline = models.TextField(blank=True, null=True, max_length=255)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(
        'StreamingPlatform', on_delete=models.CASCADE, null=True, blank=True,
        related_name='watchlist'
        )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
