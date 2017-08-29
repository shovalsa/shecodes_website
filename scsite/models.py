from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from datetime import datetime as dt
import pytz
class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    main_branch = models.ForeignKey('Branch', blank=True, default=1) # this is a many-to-one relation, which means that many users can be in the same branch
    track = models.ForeignKey('Track', blank=True, default=1)
    personal_background = models.TextField('Personal Background', max_length=2000, blank=True)
    personal_background_hebrew = models.TextField('Personal Background', max_length=2000, blank=True)

    def __str__(self):
        """
        the str is also important for the admin GUI where it allows to distinguish between items.
        """
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Track(models.Model):
    trackName = models.CharField(max_length=80)
    trackName_hebrew = models.CharField(max_length=80, null=True, blank=True, default="NA")
    trackDescription = models.TextField(default="NA")
    trackDescription_hebrew = models.TextField(default="NA", null=True, blank=True)
    # trackLogo = models.ImageField(upload_to='static/track icons', default="/static/favicon.ico")

    def __str__(self):
        return self.trackName
    #
    class Meta:
        ordering = ('trackName',)


class Branch(models.Model):
    branchName = models.CharField(max_length=80)
    branchName_hebrew = models.CharField(max_length=80, default="NA")
    areas = ((None, _("Area")), ('south', 'South'), ('tel-aviv', 'Tel Aviv'), ('center', 'Center'), ('jerusalem', 'Jerusalem'), ('north', 'North'),)
    areas_hebrew = ((None, _("אזור")), ('south', 'דרום'), ('tel-aviv', 'תל אביב'), ('center', 'מרכז'), ('jerusalem', 'ירושלים'), ('north', 'צפון'),)
    area = models.CharField(max_length=15, choices=areas, null=True)
    area_hebrew = models.CharField(max_length=15, choices=areas_hebrew, null=True)
    address = models.CharField(max_length=200, default="NA")
    address_hebrew = models.CharField(max_length=200, default="NA")
    activityTimes = models.CharField(default=_('NA'), max_length=80, help_text="e.g. Mondays at 18:30")
    activityTimes_hebrew = models.CharField(default='NA', max_length=80, help_text="למשל ימי שני ב-18:30")
    availableTracks = models.ManyToManyField(Track)
    nextGeneration = models.BooleanField(default=False)
    facebookGroup = models.URLField(default="#")
    dogs_friendly = models.BooleanField(default=False)
    children_friendly = models.BooleanField(default=False)
    Parking = models.CharField(max_length=200, default="NA")
    Parking_hebrew = models.CharField(max_length=200, default="NA")
    staff_members = models.CharField(max_length=200, default="NA")
    staff_members_hebrew = models.CharField(max_length=200, default="NA")
    track_openning_time = models.DateField(default=timezone.now)
    # how to insert items into such a model: https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/

    def __str__(self):
        return self.branchName

    class Meta:
        ordering = ('-area', 'branchName', )

class Team(models.Model):
    team_id = models.IntegerField('team_id', unique=True)
    column = models.IntegerField('column')
    name = models.CharField('Name', max_length=80)
    name_hebrew = models.CharField('שם', max_length=80, default="NA")
    title = models.CharField('Title', max_length=200)
    title_hebrew = models.CharField('תפקיד', max_length=200, default="NA")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['team_id']

class Faq(models.Model):
    question = models.CharField('Question', max_length=150)
    question_hebrew = models.CharField('שאלה', max_length=150, default="NA")
    answer = models.TextField('Answer', max_length=5000)
    answer_hebrew = models.TextField('תשובה', max_length=5000, default="NA")

    def __str__(self):
        return self.question

class News(models.Model):
    itemTitle = models.CharField(max_length=50, default="NA")
    itemTitle_hebrew = models.CharField(max_length=50, default="NA")
    itemContent = models.TextField(default="NA")
    itemContent_hebrew = models.TextField(default="NA")
    itemPhoto = models.CharField(max_length=50, default="pic1.jpg")


    def __str__(self):
        return self.itemTitle

class Job(models.Model):
    jobTitle = models.CharField(max_length=50, default=_("NA"))
    jobTitle_hebrew = models.CharField(max_length=50, default="NA")
    jobDescription = models.TextField(default=_("NA"))
    jobDescription_hebrew = models.TextField(default="NA")
    jobPhoto = models.CharField(max_length=50, default="pic1.jpg")
    jobLink = models.TextField(default="#")
    is_senior = ((None, _("Required skill level")), ('junior', _('Junior')), ('senior', _('Senior')), ('teamLeader', _('Team Leader')),)
    jobSkills = models.CharField(max_length=150, default="NA", help_text="front end / data science / DevOps etc.") #In the future, for the sake of searching, it better be m2m item
    seniority = models.CharField(max_length=150, choices=is_senior, null=True)

    def __str__(self):
        return self.jobTitle

class Event(models.Model):
    eventTitle = models.CharField(max_length=50, default="NA")
    eventTitle_hebrew = models.CharField(max_length=50, default="NA")
    eventDescription = models.TextField(default="NA")
    eventDescription_hebrew = models.TextField(default="NA")
    eventPhoto = models.ImageField(upload_to = 'static/images/events')
    eventLink = models.TextField(default="#")
    event_date = models.DateTimeField()
    eventLocation = models.CharField(max_length=100, default="NA") #Are the events always in existing branches? If so, better be FK.
    eventLocation_hebrew = models.CharField(max_length=100, default="NA") #Are the events always in existing branches? If so, better be FK.

    def __str__(self):
        return self.eventTitle

    def is_upcoming(self):
        now = dt.now()
        eventTime = self.event_date
        return eventTime >= now
