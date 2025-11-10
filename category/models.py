from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title   = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def linkcat(self):
        return reverse('category', kwargs={'title':self.title})


    def __str__(self):
        return self.title[:30]
