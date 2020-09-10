from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos')
    published = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
