from django.contrib import admin
from django.db.models.fields import json

from .models import Category, Job


admin.site.register(Job)
admin.site.register(Category)

# Register your models here.
