from django.db import models

# Create your models here.
class Post(models.Model):
    tag = models.CharField(max_length=200, null=True, blank=True)
    title= models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date  = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.title












