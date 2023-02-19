from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
import os
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    phoneId = models.CharField(null=True, blank=True, max_length=200)

    #utility Variable
    uniqueId = models.CharField(null=True, blank=True, unique=True, max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)

class InstructionContext(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    instruction = models.TextField(null=True, blank=True)

    #utility Variable
    uniqueId = models.CharField(null=True, blank=True, unique=True, max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.last_updated = timezone.localtime(timezone.now())
        super(InstructionContext, self).save(*args, **kwargs)