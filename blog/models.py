from django.db import models


class Content(models.Model):
    link = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    post = models.TextField()

    def __str__(self):
        return self.link
