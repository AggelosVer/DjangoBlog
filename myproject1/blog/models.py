from django.db import models
from  django.conf import settings
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

class Status(models.TextChoices):
    DRAFT= "DF", "Draft"
    PUBLISHED = "P", "Published"

# Create your models here.
class Post(models.Model):
 author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 title = models.CharField(max_length=255)
 slug= models.SlugField()
 body = models.TextField()
 publish = models.DateTimeField()
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)
 status = models.CharField(max_length=2,choices=Status.choices, default=Status.DRAFT)
 tags = TaggableManager()

 
 def get_absolute_url(self):
     return reverse('blog:post_detail', args=[
        self.publish.year,
        self.publish.month,
        self.publish.day,
        self.slug
    ])
 

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']