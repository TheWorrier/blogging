from django.contrib import admin
from .models import Person, Post, BlogComment
# Register your models here.

admin.site.register(Person)
admin.site.register((Post, BlogComment))