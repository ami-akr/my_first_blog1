from django.db import models

# Create your models here.
class SettingSite(models.Model):
    fotter_title       = models.CharField(max_length=120)
    fotter_description = models.TextField(default="Sign up for free and be the first to get notified about new posts.")
    facebook_url       = models.URLField(null=True, blank=True)
    twitter_url        = models.URLField(null=True, blank=True)
    youtube_url        = models.URLField(null=True, blank=True)
    telegram_url       = models.URLField(null=True, blank=True)
    instagram_url      = models.URLField(null=True, blank=True)

    def __str__(self):
        return "sitting site"