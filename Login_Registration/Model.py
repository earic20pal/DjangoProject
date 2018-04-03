from django.db import models
from django.urls import reverse

class SiddhuModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    emailid = models.CharField(max_length=20)

def __unicode__(self):
    return self.name

def get_absolute_url(self):
    return reverse('siddhu_update', kwargs={'pk': self.pk})