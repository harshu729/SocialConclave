from django.db import models
from phone_field import PhoneField
from django.core import validators

# Create your models here.


class Delegate(models.Model):
    topic = (
        ('CLIMATE ACTION', 'CLIMATE ACTION'),
        ('FINANCIAL INDEPENDENCE OF WOMEN', 'FINANCIAL INDEPENDENCE OF WOMEN'),
        ('RURAL ILLITERACY AND UNEMPLOYMENT', 'RURAL ILLITERACY AND UNEMPLOYMENT'),
        ('YOUTH PRIVACY AND SOCIAL MEDIA', 'YOUTH PRIVACY AND SOCIAL MEDIA'),
        ('ZERO HUNGER', 'ZERO HUNGER'),
    )
    genderChoices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(
        blank=False, choices=genderChoices, max_length=200, default=None)
    address = models.TextField(blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=200,  blank=True)
    topicPref1 = models.CharField(
        max_length=2000, choices=topic,  blank=False, default=None)
    topicPref2 = models.CharField(
        max_length=2000, choices=topic,  blank=False, default=None)
    topicPref3 = models.CharField(
        max_length=2000, choices=topic,  blank=False, default=None)
    age = models.IntegerField(null=True)
    schoolName = models.CharField(max_length=1000, blank=True)
    courseName = models.CharField(max_length=1000, blank=True)
    yearGrad = models.IntegerField(validators=[validators.MinValueValidator(
        999), validators.MaxValueValidator(10000)], blank=True)
    city = models.CharField(max_length=1000, blank=True)
