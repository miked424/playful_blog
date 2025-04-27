from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    # A simple category model to group blog posts
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
