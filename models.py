from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    entry = models.OneToOneField("Entry")

class Entry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name_plural = "entries"

    def __unicode__(self):
        return "%s %s"%(self.last_name, self.first_name)
