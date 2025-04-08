from django.db import models
from  django.conf import settings
from django.urls import reverse

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

 
 def get_absolute_url(self):
     return reverse('blog:post_detail', args=[
        self.publish.year,
        self.publish.month,
        self.publish.day,
        self.slug
    ])