from django.contrib import admin

# Register your models here.
from .models import User, Branch, Track, Team, Faq

admin.site.register((User, Branch, Track, Team, Faq))