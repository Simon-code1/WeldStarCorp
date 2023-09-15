from django.contrib import admin

# Register your models here.
from .models import *

class ProjectImageInline(admin.TabularInline):  
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)