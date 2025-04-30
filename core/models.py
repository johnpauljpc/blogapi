from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

USER = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,  unique=True)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1

            while Post.objects.filter(slug = slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
    
    
   
    