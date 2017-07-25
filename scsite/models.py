from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
# from datetime import *
# from django.contrib.auth.models import AbstractBaseUser as User
# Create your models here.

# class User(User.AbstractBaseUser):
#     # email = User.get_email_field_name()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['email', 'name']
#     name = models.CharField(max_length=100, blank=True, null=True)
"""
 At some point the local User class needs to be replaced with the django authenticated version.
"""

class User(models.Model):
    first_name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    main_branch = models.ForeignKey('Branch') # this is a many-to-one relation, which means that many users can be in the same branch
    track = models.ForeignKey('Track')
    personal_background = models.CharField(max_length=2000)
    join_date = models.DateTimeField()
    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def __str__(self):
        full_name = "%s %s"%(self.first_name, self.surname)
        return (full_name)

class Track(models.Model):
    trackName = models.CharField(max_length=80)
    trackDescription = models.TextField(default="N/A")
    # trackLogo = models.ImageField(upload_to='static/track icons', default="/static/favicon.ico")

    def __str__(self):
        return self.trackName
    #
    # class Meta:
    #     ordering = ('trackName',)


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

class Job(models.Model):
    jobTitle = models.CharField(max_length=50, default="Job title")
    jobDescription = models.TextField(default="Description")
    jobPhoto = models.CharField(max_length=50, default="pic1.jpg")
    jobLink = models.TextField(default="#")
    jobSkills = models.CharField(max_length=150, default="front end / data science / DevOps etc.") #In the future, for the sake of searching, it better be m2m item
    seniority = models.CharField(max_length=150, default="Junior / Senior / Team Leader etc.") #In the future, for the sake of searching, it better be m2m item

class Event(models.Model):
    eventTitle = models.CharField(max_length=50, default="Event title")
    eventDescription = models.TextField(default="Description")
    eventPhoto = models.CharField(max_length=50, default="pic1.jpg")
    eventLink = models.TextField(default="#")
    event_date = models.DateTimeField(default=timezone.now())
    # eventLocation = models.CharField(max_length=100, default="Israel") #Are the events always in existing branches? If so, better be FK.

    def is_upcoming(self):
        now = timezone.now()
        return self.event_date >= now
