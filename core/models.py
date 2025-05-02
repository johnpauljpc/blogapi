from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.exceptions import ValidationError

USER = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,  unique=True)
    content = models.TextField()
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def clean(self):
        if not self.content:
            raise ValidationError("content cannot be empty!")
    
    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1

            while Post.objects.filter(slug = slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug

        self.full_clean() #To ensure clean method is always called.
        super().save(*args, **kwargs)
        
    
    
   
    