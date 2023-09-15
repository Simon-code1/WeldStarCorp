from django.db import models
from django.db.models import Model
from django.utils.text import slugify
from multiupload.fields import MultiImageField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    image = models.ImageField(null=True, upload_to='project_images/')
    slug = models.SlugField(max_length = 200,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')