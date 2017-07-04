from django.db import models
from django.core.validators import MaxValueValidator
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
    address = models.ForeignKey('Address')
    activityTimes = models.CharField(default='למשל, ימי שני 19:30-22:00', max_length=80)
    availableTracks = models.ManyToManyField(Track)
    # how to insert items into such a model: https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/


    def __str__(self):
        return self.branchName

    class Meta:
        ordering = ('branchName',)


class Address(models.Model):
    street = models.CharField(max_length=80)
    stNumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    city = models.CharField(max_length=40)
    postalCode = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    country = models.CharField(max_length=80, default='ישראל', editable=False)

    def __str__(self):
        return ('%s %s, \n%s, %s %s'%(self.street, self.stNumber, self.city, self.postalCode, self.country))

class Team(models.Model):
    team_id = models.IntegerField('team_id', unique=True)
    column = models.IntegerField('column')
    name = models.CharField('Name', max_length=80)
    title = models.CharField('Title', max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['team_id']