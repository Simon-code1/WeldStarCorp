from django.db import models
from django.db.models import Model
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    slug = models.SlugField(max_length = 200,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name