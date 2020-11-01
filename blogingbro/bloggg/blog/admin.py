from django.contrib import admin
from .models import Person, Post, Like, BlogComment
# Register your models here.

admin.site.register(Person)
admin.site.register(Post)
admin.site.register((Like))
admin.site.register((BlogComment))