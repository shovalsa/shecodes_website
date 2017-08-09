from __future__ import unicode_literals
import re
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    main_branch = models.ForeignKey('Branch', blank=True, default=1) # this is a many-to-one relation, which means that many users can be in the same branch
    track = models.ForeignKey('Track', blank=True, default=1)
    personal_background = models.TextField(max_length=2000, blank=True)
    join_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        the str is also important for the admin GUI where it allows to distinguish between items.
        """
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

class Track(models.Model):
    trackName = models.CharField(max_length=80)
    trackDescription = models.TextField(default="N/A")
    # trackLogo = models.ImageField(upload_to='static/track icons', default="/static/favicon.ico")

    def __str__(self):
        return self.trackName
    #
    class Meta:
        ordering = ('trackName',)


class Branch(models.Model):
    branchName = models.CharField(max_length=80)
    area = models.CharField(max_length=200, default="NA")
    address = models.CharField(max_length=200, default="NA")
    activityTimes = models.CharField(default='למשל, ימי שני 19:30-22:00', max_length=80)
    availableTracks = models.ManyToManyField(Track)
    nextGeneration = models.CharField(max_length=2, default="NA")
    facebookGroup = models.CharField(max_length=500, default="NA")
    dogs_friendly = models.CharField(max_length=200, default="NA")
    children_friendly = models.CharField(max_length=200, default="NA")
    Parking = models.CharField(max_length=200, default="NA")
    managers = models.CharField(max_length=200, default="NA")
    other_staff_members = models.CharField(max_length=200, default="NA")
    # how to insert items into such a model: https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/


    def __str__(self):
        return self.branchName

    class Meta:
        ordering = ('branchName',)

class Team(models.Model):
    team_id = models.IntegerField('team_id', unique=True)
    column = models.IntegerField('column')
    name = models.CharField('Name', max_length=80)
    title = models.CharField('Title', max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['team_id']

class Faq(models.Model):
    question = models.CharField('Question', max_length=150)
    answer = models.TextField('Answer', max_length=5000)

    def __str__(self):
        return self.question

class News(models.Model):
    itemTitle = models.CharField(max_length=50, default="Item title")
    itemContent = models.TextField(default="content")
    itemPhoto = models.CharField(max_length=50, default="pic1.jpg")

    def __str__(self):
        return self.itemTitle

class Job(models.Model):
    jobTitle = models.CharField(max_length=50, default="Job title")
    jobDescription = models.TextField(default="Description")
    jobPhoto = models.CharField(max_length=50, default="pic1.jpg")
    jobLink = models.TextField(default="#")
    is_senior = ((None, "Required skill level"), ('junior', 'Junior'), ('senior', 'Senior'), ('teamLeader', 'Team Leader'),)
    jobSkills = models.CharField(max_length=150, default="front end / data science / DevOps etc.") #In the future, for the sake of searching, it better be m2m item
    seniority = models.CharField(max_length=150, choices=is_senior, null=True)

    def __str__(self):
        return self.jobTitle

class Event(models.Model):
    eventTitle = models.CharField(max_length=50, default="Event title")
    eventDescription = models.TextField(default="Description")
    eventPhoto = models.CharField(max_length=50, default="pic1.jpg")
    eventLink = models.TextField(default="#")
    event_date = models.DateTimeField(default=timezone.now)
    # eventLocation = models.CharField(max_length=100, default="Israel") #Are the events always in existing branches? If so, better be FK.

    def __str__(self):
        return self.eventTitle

    def is_upcoming(self):
        now = timezone.now()
        return self.event_date >= now
