from django.contrib import admin

# Register your models here.
from .models import User, Branch, Track, Address, Team

admin.site.register((User, Branch, Track, Address, Team))