from django.contrib import admin
from .models import Pet, Post, Photo, Reply

# Register your models here.
admin.site.register(Pet)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Reply)
