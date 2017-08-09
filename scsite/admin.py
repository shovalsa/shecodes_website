from django.contrib import admin

# Register your models here.
from .models import Profile, Branch, Track, Team, Faq, News, Job, Event

admin.site.register((Profile, Branch, Track, Team, Faq, News, Job, Event))