from django.contrib import admin

# Register your models here.
from .models import User, Branch, Track, Address

admin.site.register((User, Branch, Track, Address))