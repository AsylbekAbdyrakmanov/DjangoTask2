from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    book = models.FileField(upload_to='posts/files/')
    description = models.TextField()
    image = models.ImageField(upload_to='posts/cover', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

