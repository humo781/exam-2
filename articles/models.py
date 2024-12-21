from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    short_content = models.CharField(max_length=100)
    long_content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateField(default=timezone.now)

    def get_detail_url(self):
        return reverse('articles:detail', args=[self.pk])
