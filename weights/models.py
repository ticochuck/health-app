from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.CharField(max_length=6)
    date_posted = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)


    def __str__(self):
        return f'{self.user}, {self.weight}'


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk})
    



