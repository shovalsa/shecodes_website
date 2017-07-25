from django.contrib import admin

# Register your models here.
from .models import User, Branch, Track, Team, Faq, News, Job, Event

admin.site.register((User, Branch, Track, Team, Faq, News, Job, Event))