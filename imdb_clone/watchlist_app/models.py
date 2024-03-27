from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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


class Reviews(models.Model):
    watchlist = models.ForeignKey(
        'WatchList', on_delete=models.CASCADE, null=True, blank=True,
        related_name='reviews'
        )
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + ' - ' + self.watchlist.title