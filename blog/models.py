from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def generate_slug(s):
    return slugify(s, allow_unicode=True) + '-' + str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name='posts')
    pub_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
        
    
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})    

    def __str__(self):
        return self.title
    