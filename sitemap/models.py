from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    identifier = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=200, null=True)

    def get_absolute_url(self):
        return reverse("blog", args=[(self.identifier)])
