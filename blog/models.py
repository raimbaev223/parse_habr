from django.db import models
from django.urls import reverse


class Content(models.Model):
    link = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    post = models.TextField()

    def __str__(self):
        return self.link

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

    class Meta:
        ordering = ['id',]
